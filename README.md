# YouTube Interview Summarizer

> An AI-native skill for extracting deep, structured intelligence from long-form YouTube interviews — built for Antigravity and compatible AI agents.

---

## What This Does

This is a **prompt engineering skill** that instructs an AI agent to:

1. Fetch a YouTube video transcript (via the `youtube-transcript` sub-skill)
2. Determine the appropriate summary mode (short thesis-driven vs. exhaustive chronological deep-dive) based on video length
3. Extract all high-value evidence as structured blocks with **original English quotes + faithful Chinese translation**
4. Export the final summary to a clean, well-formatted **PDF**

The core design principle is **Uncapped Linear Scale-to-Length**: the longer the video, the more evidence blocks are extracted — no artificial limits, no token-saving compression.

---

## Key Features

- ✅ **Evidence-First**: Every claim is backed by a verbatim original quote (2–5 sentences of context)
- ✅ **Authentic Tone Protocol**: Translations are objective, analytical, and literal — no dramatization, no editorial embellishment
- ✅ **Dynamic Scaling**: Summary length scales linearly with video duration (a 2-hour video produces ~2× the output of a 1-hour video)
- ✅ **Time-Stamped Chronological Mode**: For long interviews, extracts chapter-by-chapter with timestamps
- ✅ **PDF Export**: One polished PDF per video with Chinese title, clean typography

---

## File Structure

```
youtube-interview-summarizer/
├── README.md
├── LICENSE
├── skills/
│   └── video-summary/
│       └── SKILL.md           # Main workflow entrypoint for AI agents
├── guidelines/
│   └── summary_guidelines.md  # Complete extraction rules, translation protocol, and output format spec
└── examples/
    └── sample_output.md       # Example output from a real interview (Dylan Patel, AI infrastructure)
```

---

## How to Use

### Prerequisites

This skill is designed to run inside an **AI agent environment** (e.g., Antigravity, Claude, or any agent that supports tool-calling and file I/O).

You will also need:
- The [`youtube-transcript`](https://github.com/jdepoix/youtube-transcript-api) capability (or equivalent) to fetch captions
- A PDF rendering tool (optional — for the `md-to-pdf` export step)

### Quickstart

1. Copy `skills/video-summary/SKILL.md` and `guidelines/summary_guidelines.md` into your agent's skills directory
2. Point your agent at a YouTube URL
3. The agent will automatically:
   - Fetch the transcript
   - Choose the right summary mode
   - Output a structured Markdown file
   - (Optionally) export to PDF

### Customization

| What you want to change | Where to edit |
|---|---|
| Summary structure, extraction rules | `guidelines/summary_guidelines.md` |
| Workflow steps, verification logic | `skills/video-summary/SKILL.md` |
| Translation tone, banned terms | `guidelines/summary_guidelines.md` → `AUTHENTIC & OBJECTIVE TRANSLATION PROTOCOL` |

---

## Design Philosophy

Most AI video summarizers either produce shallow bullet points or lose the speaker's original voice through over-paraphrasing.

This skill is built on the opposite belief:

> **The original words are the evidence. The translation is just a lens.**

All summaries:
- Preserve 3–5 sentences of original context around every key claim
- Use dry, analytical Chinese — not clickbait headlines
- Scale in proportion to the actual information density of the video

---

## Example Output

See [`examples/sample_output.md`](examples/sample_output.md) for a real summary generated from Dylan Patel's 2.5-hour interview on AI infrastructure bottlenecks.

---

## License

MIT — free to use, modify, and build on.

---

## Author

[@max-tutu-dev](https://github.com/max-tutu-dev)
