---
name: md-to-pdf
description: Convert Markdown files to styled PDF documents using a Python HTML generator and headless Chrome.
---

# Markdown to PDF Conversion Skill

Use this skill to convert Markdown documents (e.g., summaries, reports) into professionally styled PDF files.

## Workflow

1) **Check Requirements**:
   - Ensure the `markdown` Python package is installed (`pip3 install markdown`).
   - Ensure Google Chrome is installed at `/Applications/Google Chrome.app`.

2) **Generate HTML**:
   - Use the internal script `scripts/convert_to_html.py` to convert the `.md` file to `.html`.
   - The script automatically injects:
     - A **branded cover page** (dark gradient background, top ribbon, title, meta tags, video URL chip)
     - **Author & Project card** at cover bottom (author info + GitHub project)
     - Professional body CSS (Inter typography, blue blockquotes, striped tables, clean margins)
     - **No page headers/footers** — removes Chrome's default file path printing
   - The cover page auto-extracts:
     - **Video URL**: if the first line of the `.md` file starts with `http`, it appears as a chip on the cover
     - **Document title**: the first `# H1` heading becomes the cover page title

3) **Print to PDF**:
   - Run Google Chrome in headless mode:
     ```bash
     "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu --print-to-pdf="output.pdf" "input.html"
     ```

4) **Cleanup**:
   - Remove the temporary `.html` file after conversion.

## Internal Tools

- `scripts/convert_to_html.py`: MD-to-HTML conversion with branded cover page injection and full CSS theme.

## Cover Page Features

The cover page includes:
- **Top ribbon**: "AI 访谈深度精译系列 · AI Interview Intelligence Series"
- **Title**: Extracted from first `# H1` heading
- **Meta tags**: 证据驱动 · 原话引用 · 精准翻译 · 客观无演绎
- **URL chip**: Video source link (if provided)
- **Author card**: Author name and contact (Max. Zheng, WeChat)
- **GitHub project card**: youtube-interview-summarizer @ github.com/max-tutu-dev

## Markdown Formatting Notes for Best Results

- Put the YouTube URL as **the very first line** of the `.md` file (before any headings) — it will appear as a source chip on the cover.
- The first `# H1` heading is used as the cover title — make it descriptive.
- Use `>` blockquotes for all original quotes (render with blue left border on light blue background).

## PDF Output Characteristics

- **No file path in headers/footers** — pages are clean without local path information
- **Proper margins** — content has breathing room at page edges
- **Cover page separation** — cover is its own page, content starts fresh

## Last Updated

- 2026-03-24: Added author/GitHub card, removed page footers, improved margins