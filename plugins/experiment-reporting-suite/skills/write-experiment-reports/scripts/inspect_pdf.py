"""Run structural checks on a report PDF and optionally create a contact sheet."""

from __future__ import annotations

import argparse
import math
import re
from pathlib import Path

import fitz


UNRESOLVED_PATTERNS = {
    "template placeholder": re.compile(r"\{\{.+?\}\}"),
    "math placeholder": re.compile(r"REPORTMATH(?:DISPLAY|INLINE)?TOKEN"),
    "KaTeX error": re.compile(r"KaTeX parse error|katex-error", re.IGNORECASE),
    "unfinished marker": re.compile(r"\[(?:TODO|NEEDS INPUT):", re.IGNORECASE),
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--contact-sheet", type=Path)
    parser.add_argument("--expect-heading", action="append", default=[])
    parser.add_argument(
        "--blank-ink-threshold",
        type=float,
        default=0.0005,
        help="minimum non-white pixel fraction for a page (default: 0.0005)",
    )
    return parser


def page_ink_fraction(page: fitz.Page) -> float:
    matrix = fitz.Matrix(0.25, 0.25)
    pixmap = page.get_pixmap(matrix=matrix, colorspace=fitz.csGRAY, alpha=False)
    samples = pixmap.samples
    nonwhite = sum(value < 250 for value in samples)
    return nonwhite / max(1, len(samples))


def make_contact_sheet(document: fitz.Document, output: Path) -> None:
    try:
        from PIL import Image, ImageDraw
    except ImportError as exc:
        raise RuntimeError(
            "Pillow is required for --contact-sheet; install scripts/requirements.txt"
        ) from exc

    thumbnails: list[Image.Image] = []
    for page in document:
        pixmap = page.get_pixmap(matrix=fitz.Matrix(0.6, 0.6), alpha=False)
        image = Image.frombytes("RGB", (pixmap.width, pixmap.height), pixmap.samples)
        thumbnails.append(image)

    columns = min(4, max(1, len(thumbnails)))
    rows = math.ceil(len(thumbnails) / columns)
    cell_width = max(image.width for image in thumbnails) + 24
    cell_height = max(image.height for image in thumbnails) + 44
    sheet = Image.new("RGB", (columns * cell_width, rows * cell_height), "white")
    draw = ImageDraw.Draw(sheet)
    for index, image in enumerate(thumbnails):
        x = (index % columns) * cell_width + 12
        y = (index // columns) * cell_height + 28
        sheet.paste(image, (x, y))
        draw.text((x, 8 + (index // columns) * cell_height), f"Page {index + 1}", fill="black")
    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output)


def main() -> None:
    args = build_parser().parse_args()
    pdf_path = args.pdf.expanduser().resolve()
    if not pdf_path.is_file() or pdf_path.stat().st_size == 0:
        raise FileNotFoundError(f"non-empty PDF not found: {pdf_path}")

    failures: list[str] = []
    with fitz.open(pdf_path) as document:
        if document.page_count == 0:
            failures.append("PDF has no pages")
        text = "\n".join(page.get_text() for page in document)
        blank_pages = [
            index + 1
            for index, page in enumerate(document)
            if page_ink_fraction(page) < args.blank_ink_threshold
        ]
        if blank_pages:
            failures.append(f"likely blank pages: {blank_pages}")

        for label, pattern in UNRESOLVED_PATTERNS.items():
            if pattern.search(text):
                failures.append(f"found {label}")
        for heading in args.expect_heading:
            if heading.casefold() not in text.casefold():
                failures.append(f"missing expected heading: {heading!r}")

        if args.contact_sheet is not None:
            contact_sheet = args.contact_sheet.expanduser().resolve()
            make_contact_sheet(document, contact_sheet)
            print(f"Contact sheet: {contact_sheet}")

        print(f"PDF: {pdf_path}")
        print(f"Pages: {document.page_count}")
        print(f"Text characters: {len(text)}")
        print(f"Likely blank pages: {blank_pages or 'none'}")

    if failures:
        raise SystemExit("PDF validation failed: " + "; ".join(failures))
    print("PDF validation passed")


if __name__ == "__main__":
    main()
