---
name: interview-intelligence-suite
description: Complete workflow for AI interview video summarization and PDF export. Combines video-summary (evidence-first deep-dive) and md-to-pdf (branded PDF generation).
---

# Interview Intelligence Suite

A complete end-to-end system for summarizing AI interview videos and exporting them as professionally branded PDF reports.

## Overview

This suite consists of two integrated skills:

1. **video-summary**: Deep-dive video summarization using evidence-first protocol (V4 Dynamic Scale-to-Length)
2. **md-to-pdf**: Convert markdown summaries to branded PDF documents

## Workflow

### Step 1: Summarize the Video

Use the `video-summary` skill to:
- Extract transcript (from YouTube or provided file)
- Follow `summary_guidelines.md` (evidence-first protocol)
- Generate comprehensive markdown summary with:
  - Speaker insight & bias analysis
  - Key signals & data (all quantitative facts)
  - V4 Dynamic Scale-to-Length deep-dive (time-block chronological extraction)
  - Research layer (NotebookLM follow-up questions)

**Output**: Markdown file (`.md`)

### Step 2: Convert to PDF

Use the `md-to-pdf` skill to:
- Convert markdown to HTML with branded cover page
- Print to PDF via headless Chrome
- Auto-extract video URL and document title

**Output**: Professional PDF with:
- Dark gradient cover page
- Top ribbon: "AI 访谈深度精译系列"
- Meta tags: 证据驱动 · 原话引用 · 精准翻译 · 客观无演绎
- Author card (Max. Zheng, WeChat)
- GitHub project card
- Clean typography (Inter font, blue blockquotes, striped tables)

## Key Features

### Evidence-First Protocol

- **No dramatization**: Objective, literal, faithful translations
- **Quantitative focus**: All numbers, costs, milestones extracted
- **Context preservation**: 3-5 sentence quote blocks with full logic chain
- **Density scaling**: Output length scales linearly with video duration (no arbitrary limits)

### PDF Branding

- **Cover page**: Dark gradient with decorative circles
- **Typography**: Inter font, professional spacing
- **No file paths**: Clean pages without local path printing
- **Metadata**: Video URL chip, author info, GitHub project

## File Structure

```
interview-intelligence-suite/
├── SKILL.md (this file)
├── video-summary/
│   ├── SKILL.md
│   └── summary_guidelines.md
└── md-to-pdf/
    ├── SKILL.md
    └── scripts/
        └── convert_to_html.py
```

## Usage Example

1. **Summarize video**:
   - Provide YouTube URL or transcript file
   - Skill extracts and summarizes per evidence-first protocol
   - Output: `[中文标题] + [核心论点].md`

2. **Convert to PDF**:
   - Pass markdown file to md-to-pdf skill
   - Skill generates branded PDF
   - Output: `[中文标题] + [核心论点].pdf`

## Dependencies

- Python 3 with `markdown` package
- Google Chrome (at `/Applications/Google Chrome.app` on macOS)
- YouTube transcript access (for video summarization)

## Notes

- **Translation tone**: All Chinese must be objective, analytical, data-driven (no clickbait)
- **Density constraint**: Longer videos → longer summaries (linear scaling, no compression)
- **Quote blocks**: Minimum 3-5 sentences per quote (full logic chain, not just conclusions)
- **Naming convention**: `[中文视频标题] + [核心论点摘要].pdf`

## Last Updated

- 2026-03-27: Integrated video-summary + md-to-pdf into unified suite
