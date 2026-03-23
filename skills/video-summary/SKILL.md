---
name: video-summary
description: Summarize interview-style videos using [summary_guidelines.md](file:///Users/tutuzheng/.gemini/antigravity/scratch/youtube_transcripts/ai_interviews/summary_guidelines.md).
---

# Video Summary Workflow

Use this skill when the user asks for a summary of a YouTube/interview video or a transcript-based summary.

## Requirements

- Access to a transcript file (preferred) or the ability to fetch a transcript via youtube-transcript.
- Follow [summary_guidelines.md](file:///Users/tutuzheng/.gemini/antigravity/scratch/youtube_transcripts/ai_interviews/summary_guidelines.md) exactly.

## Workflow

1) Ensure a transcript is available:
- If the user provided a transcript file, use it.
- Otherwise, call youtube-transcript to download captions and clean them.

2) Build the summary strictly per [summary_guidelines.md](file:///Users/tutuzheng/.gemini/antigravity/scratch/youtube_transcripts/ai_interviews/summary_guidelines.md):
  - **DETERMINE MODE**: Decide whether to use **Mode 1 (Short/Thesis-Driven)** or **Mode 2 (V4 Dynamic Scale-to-Length Deep-Dive)**. For videos > 1 hour, or if the transcript has time chunks (e.g., `[00:00 - 00:05]`), or if the user requests time sequence, **MUST use Mode 2**.
  - **OPERATIONAL GUIDANCE FOR AGENTS**: If dealing with a video > 1 hour, **DO NOT** attempt to generate the summary in a standard conversational response due to token cutoff limits. Instead, you MUST read the transcript piecewise and directly write the massive markdown output using the `write_to_file` tool. 
  - **Speaker Insight**: Background, motive, and bias analysis.
  - **Intelligence Layer (Key Signals & Data)**: Mandatory extraction of numbers, costs, milestones, and specific terms.
  - **Logic Layer (Depending on Mode)**: Either 3-5 core theses (Mode 1) OR ultra-exhaustive chronological extraction block-by-block strictly following the Uncapped Linear Scale-to-Length principle (Mode 2).
  - **Research Layer**: Targeted follow-up questions for NotebookLM.

3) **VERIFICATION (CRITICAL)**:
   - Before generating the final file, review your extraction density. 
   - For Mode 2 on long videos, did you intelligently scale the extraction volume directly to the video's total duration without setting arbitrary limits? (e.g., A 2-hour video should produce significantly more output than a 1-hour video). If not, **FIND MORE** in the transcript.
   - **TONE CHECK**: Verify that all Chinese translations follow the **Authentic & Objective Translation Protocol** defined in `summary_guidelines.md`. Specifically: no dramatized vocabulary, no editorializing, no clickbait phrasing. The translation must faithfully mirror the speaker's original analytical, data-driven register.
   - Do not proceed until both the quantitative density constraint AND the tone constraint are met.

4) Deliverables:
- **One PDF per video** (do not consolidate).
- **Naming Convention**: `[中文视频标题] + [核心论点摘要].pdf` (e.g., `AI扩展速度超乎预期-基础设施投资合理化.pdf`).
- **Content Requirement**: 
  - The YouTube video URL must be displayed as a **raw URL** (no hyperlinks) at the very top.
  - The Document Title (H1) must be in **Chinese**.
- Default to .docx only (per guidelines).
- If asked, also export to .txt.
- **PDF Export**: If requested, use the `md-to-pdf` skill.
- When exporting to .docx/PDF, ensure modern typography and clean formatting.

## Notes

- **Translation Tone (MANDATORY)**: All Chinese translations must be **objective, faithful, and literal** — matching the speaker's original register. The speaker is a data-driven industry analyst; the output must read like a rigorous analyst report, not editorial commentary. See the `🔥 AUTHENTIC & OBJECTIVE TRANSLATION PROTOCOL` block in `summary_guidelines.md` for the specific banned terms and style rules.
- Do not add external information, personal inferences, or judgements that are not present in the original transcript.
