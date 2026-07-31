"""Render a Markdown experiment report to styled HTML and PDF."""

from __future__ import annotations

import argparse
import html
import re
import shutil
import subprocess
from pathlib import Path

from markdown_it import MarkdownIt
from mdit_py_plugins.anchors import anchors_plugin
from weasyprint import CSS, HTML


SKILL_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_STYLESHEET = SKILL_ROOT / "assets" / "report.css"
KATEX_CSS_CANDIDATES = (
    Path("/usr/share/javascript/katex/katex.min.css"),
    Path("/usr/local/lib/node_modules/katex/dist/katex.min.css"),
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--html-output", type=Path)
    parser.add_argument("--stylesheet", type=Path, default=DEFAULT_STYLESHEET)
    parser.add_argument("--katex-command", default="katex")
    parser.add_argument("--katex-css", type=Path)
    parser.add_argument("--language", default="en")
    return parser


def resolve_katex_css(explicit: Path | None) -> Path:
    if explicit is not None:
        path = explicit.expanduser().resolve()
        if not path.is_file():
            raise FileNotFoundError(f"KaTeX stylesheet not found: {path}")
        return path
    for candidate in KATEX_CSS_CANDIDATES:
        if candidate.is_file():
            return candidate
    raise FileNotFoundError(
        "KaTeX stylesheet not found; pass --katex-css /path/to/katex.min.css"
    )


def resolve_katex_command(command: str) -> str:
    path = shutil.which(command)
    if path is None:
        raise FileNotFoundError(
            f"KaTeX command not found: {command!r}; install KaTeX or pass "
            "--katex-command"
        )
    return path


def render_katex(expression: str, *, display: bool, command: str) -> str:
    invocation = [command, "--no-throw-on-error"]
    if display:
        invocation.append("--display-mode")
    result = subprocess.run(
        invocation,
        input=expression.strip(),
        text=True,
        capture_output=True,
        check=True,
    )
    rendered = result.stdout.strip()
    if "katex-error" in rendered:
        raise ValueError(f"KaTeX could not render expression: {expression.strip()}")
    return rendered


def extract_math(
    source: str, *, katex_command: str
) -> tuple[str, dict[str, tuple[str, bool]]]:
    display_pattern = re.compile(r"\\\[(.+?)\\\]", re.DOTALL)
    inline_pattern = re.compile(r"\\\((.+?)\\\)", re.DOTALL)
    replacements: dict[str, tuple[str, bool]] = {}

    def replace_display(match: re.Match[str]) -> str:
        token = f"REPORTMATHDISPLAYTOKEN{len(replacements):06d}"
        replacements[token] = (
            render_katex(match.group(1), display=True, command=katex_command),
            True,
        )
        return f"\n\n{token}\n\n"

    def replace_inline(match: re.Match[str]) -> str:
        token = f"REPORTMATHINLINETOKEN{len(replacements):06d}"
        replacements[token] = (
            render_katex(match.group(1), display=False, command=katex_command),
            False,
        )
        return token

    source = display_pattern.sub(replace_display, source)
    source = inline_pattern.sub(replace_inline, source)
    return source, replacements


def inject_math(body: str, replacements: dict[str, tuple[str, bool]]) -> str:
    for token, (rendered, display) in replacements.items():
        placeholder = f"<p>{token}</p>" if display else token
        if placeholder not in body:
            raise ValueError(f"rendered document lost math placeholder {token}")
        body = body.replace(placeholder, rendered)
    return body


def markdown_renderer() -> MarkdownIt:
    renderer = MarkdownIt(
        "commonmark",
        {
            "html": True,
            "linkify": False,
            "typographer": True,
        },
    )
    renderer.enable("table")
    renderer.enable("strikethrough")
    renderer.use(anchors_plugin, min_level=1, max_level=3)
    return renderer


def build_toc(tokens: list) -> str:
    entries = []
    for index, token in enumerate(tokens):
        if token.type != "heading_open":
            continue
        level = int(token.tag[1:])
        if level not in (2, 3):
            continue
        heading_id = token.attrGet("id")
        label = tokens[index + 1].content
        entries.append(
            '<li class="toc-level-{level}"><a href="#{target}">{label}</a></li>'.format(
                level=level,
                target=html.escape(heading_id or "", quote=True),
                label=html.escape(label),
            )
        )
    return (
        '<nav class="toc" aria-label="Table of contents">'
        "<h2>Contents</h2><ol>"
        + "".join(entries)
        + "</ol></nav>"
    )


def html_document(title: str, body: str, *, language: str) -> str:
    return f"""<!doctype html>
<html lang="{html.escape(language, quote=True)}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
</head>
<body>
{body}
</body>
</html>
"""


def main() -> None:
    args = build_parser().parse_args()
    input_path = args.input.expanduser().resolve()
    output_path = args.output.expanduser().resolve()
    stylesheet_path = args.stylesheet.expanduser().resolve()
    html_output_path = (
        args.html_output.expanduser().resolve()
        if args.html_output is not None
        else output_path.with_suffix(".html")
    )

    if not input_path.is_file():
        raise FileNotFoundError(f"Markdown input not found: {input_path}")
    if not stylesheet_path.is_file():
        raise FileNotFoundError(f"stylesheet not found: {stylesheet_path}")

    katex_command = resolve_katex_command(args.katex_command)
    katex_css = resolve_katex_css(args.katex_css)
    source = input_path.read_text(encoding="utf-8")
    titles = re.findall(r"^#\s+(.+)$", source, flags=re.MULTILINE)
    if len(titles) != 1:
        raise ValueError(f"report must contain exactly one level-1 title; found {len(titles)}")
    title = titles[0].strip()

    source_with_math, math_replacements = extract_math(
        source, katex_command=katex_command
    )
    renderer = markdown_renderer()
    tokens = renderer.parse(source_with_math)
    body = renderer.renderer.render(tokens, renderer.options, {})
    body = body.replace("<!-- PDF_TOC -->", build_toc(tokens))
    body = inject_math(body, math_replacements)
    if "REPORTMATH" in body:
        raise ValueError("unresolved math placeholder remains after rendering")
    document = html_document(title, body, language=args.language)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    html_output_path.parent.mkdir(parents=True, exist_ok=True)
    html_output_path.write_text(document, encoding="utf-8")
    HTML(string=document, base_url=str(input_path.parent)).write_pdf(
        output_path,
        stylesheets=[
            CSS(filename=str(katex_css)),
            CSS(filename=str(stylesheet_path)),
        ],
        presentational_hints=True,
    )
    print(f"HTML: {html_output_path}")
    print(f"PDF:  {output_path}")


if __name__ == "__main__":
    main()
