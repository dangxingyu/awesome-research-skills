# PDF Delivery

The bundled renderer converts CommonMark Markdown to HTML, renders
`\(...\)` and `\[...\]` through the KaTeX CLI, and writes PDF with WeasyPrint.
The PDF inspector extracts text, checks for unresolved tokens, detects likely
blank pages, and can build a contact sheet.

## Environment

Install the Python dependencies in an isolated environment:

```bash
python -m pip install -r scripts/requirements.txt
```

Install a `katex` executable and make its stylesheet available. Common Linux
locations include:

```text
/usr/share/javascript/katex/katex.min.css
/usr/local/lib/node_modules/katex/dist/katex.min.css
```

Pass nonstandard locations explicitly:

```bash
python scripts/render_report.py \
  --input report.md \
  --output report.pdf \
  --katex-command /path/to/katex \
  --katex-css /path/to/katex.min.css
```

WeasyPrint may require system libraries for Pango, Cairo, and font discovery.
Install fonts that cover the report language and math glyphs. The bundled CSS
prefers DejaVu and Noto CJK families but permits system fallbacks.

## Authoring conventions

- Use exactly one level-1 heading as the title.
- Insert `<!-- PDF_TOC -->` on its own line to place the table of contents.
- Use level-2 headings for major sections and level-3 headings for subsections.
- Use `\(...\)` for inline math and `\[...\]` for display math.
- Keep image paths relative to the Markdown source.
- Prefer tables with concise cells; move long explanations into prose.
- Give figures explicit captions in the Markdown.

Math is replaced with opaque placeholders before Markdown parsing, then
injected after the heading tree and table of contents are built. This prevents
KaTeX HTML from corrupting Markdown structure.

## Render

From the skill directory:

```bash
python scripts/render_report.py \
  --input /absolute/path/report.md \
  --output /absolute/path/report.pdf \
  --html-output /absolute/path/report.html
```

The default stylesheet is `assets/report.css`. Use `--stylesheet` to supply a
project-specific stylesheet.

## Inspect

```bash
python scripts/inspect_pdf.py report.pdf \
  --contact-sheet report-contact-sheet.png \
  --expect-heading "Executive result" \
  --expect-heading "Algorithms" \
  --expect-heading "Experiments"
```

The inspector exits nonzero for unresolved template markers, render errors,
missing expected headings, or likely blank pages. It is a preflight, not a
substitute for visual review.

Inspect:

- the contact sheet for page rhythm and accidental whitespace;
- title, contents, and first content page;
- every page containing a dense table;
- pages before and after large equations;
- every full-resolution figure and caption;
- final limitations, decision, and reproducibility pages.

After final rendering, record hashes:

```bash
sha256sum report.md report.html report.pdf
```

Record the report date, code revision, data/result manifest revision, and the
exact render command near the artifact manifest.
