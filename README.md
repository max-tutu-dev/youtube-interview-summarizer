# YouTube Interview Summarizer - OpenClaw Integration

> **AI-native skill for extracting deep, structured intelligence from long-form YouTube interviews**

✨ **Now with OpenClaw support!** Use this skill with OpenClaw agents for automated video summarization.

---

## What This Does

This is a **prompt engineering skill** that instructs an AI agent to:

1. Fetch a YouTube video transcript (via `youtube-transcript-api`)
2. Determine the appropriate summary mode based on video length:
   - **Mode 1**: Thesis-driven (short videos < 1 hour)
   - **Mode 2**: Full panoramic timestamp recap (long videos ≥ 1 hour)
3. Extract all high-value evidence as structured blocks with **original English quotes + faithful Chinese translation**
4. Export the final summary to Markdown

### Core Design Principle

**🎯 Uncapped Linear Scale-to-Length**: The longer the video, the more evidence blocks are extracted — no artificial limits, no token-saving compression.

---

## Key Features

- ✅ **Evidence-First**: Every claim backed by verbatim original quotes (2–5 sentences of context)
- ✅ **Authentic Tone Protocol**: Translations are objective, analytical, and literal — no dramatization
- ✅ **Dynamic Scaling**: Summary length scales linearly with video duration
- ✅ **Time-Stamped Chronological Mode**: Chapter-by-chapter extraction for long interviews
- ✅ **Multi-Platform Support**: Works with Antigravity, OpenClaw, and compatible AI agents

---

## Quick Start

### Option 1: OpenClaw Users

1. **Install youtube-transcript-api**:
   ```bash
   pip3 install --break-system-packages youtube-transcript-api
   ```

2. **Install the skill**:
   ```bash
   cp -r youtube-interview-summarizer ~/.openclaw/skills/
   ```

3. **Use it**:
   ```
   总结这个访谈：https://youtu.be/rIwgZWzUKm8
   ```

See [OPENCLAW_INTEGRATION.md](OPENCLAW_INTEGRATION.md) for detailed OpenClaw setup.

### Option 2: Other AI Agents

1. Copy `skills/video-summary/SKILL.md` and `guidelines/summary_guidelines.md` to your agent's skills directory
2. Ensure your agent has `youtube-transcript` capability
3. Point your agent at a YouTube URL

---

## Example Output

See [`examples/sample_output.md`](examples/sample_output.md) for a real summary from Dylan Patel's 2.5-hour interview on AI infrastructure.

### Sample Structure

```markdown
# Interview Title

> **Source**: [YouTube URL]
> **Duration**: X hours
> **Summary Mode**: Mode 2 - Full Panoramic Timestamp Recap

## Speaker Background
[Bio and "position" (where they're coming from)]

## Hard Signals & Data
[Quantified facts, funding, career milestones]

## Core Arguments / Time-Stamped Chapters
- Chapter 1: [Topic] [00:00-45:00]
  - Claim: [Argument]
  - Evidence: [Original quote 2-5 sentences]

## Research Questions for Deep Dive
[NotebookLM-style follow-up questions]
```

---

## File Structure

```
youtube-interview-summarizer/
├── README.md                        # This file
├── OPENCLAW_INTEGRATION.md          # OpenClaw setup guide
├── LICENSE
├── OPENCLAW_SKILL.md                # OpenClaw skill definition
├── skills/
│   └── video-summary/
│       └── SKILL.md                 # Original Antigravity skill
├── guidelines/
│   └── summary_guidelines.md        # Complete extraction rules
└── examples/
    └── sample_output.md             # Example summary
```

---

## Design Philosophy

> **The original words are the evidence. The translation is just a lens.**

Most AI video summarizers either produce shallow bullet points or lose the speaker's original voice through over-paraphrasing.

This skill is built on the opposite belief:

- ✅ Preserve 3–5 sentences of original context around every key claim
- ✅ Use dry, analytical Chinese — not clickbait headlines
- ✅ Scale in proportion to actual information density

---

## Performance Benchmarks

| Video Length | Evidence Blocks | Output Words |
|--------------|-----------------|--------------|
| 15 minutes   | 5-8             | ~1,500       |
| 1 hour       | 12-18           | ~4,000       |
| 2.5 hours    | 25-35           | ~10,000      |
| 7 hours      | 50+             | ~40,000      |

---

## Customization

| What you want to change | Where to edit |
|---|---|
| Summary structure, extraction rules | `guidelines/summary_guidelines.md` |
| Workflow steps, verification logic | `skills/video-summary/SKILL.md` or `OPENCLAW_SKILL.md` |
| Translation tone, banned terms | `guidelines/summary_guidelines.md` → "AUTHENTIC & OBJECTIVE TRANSLATION PROTOCOL" |
| Output directory (OpenClaw) | `OPENCLAW_SKILL.md` → "Default Output Paths" |

---

## Three Core Principles

### 1. Evidence-First Principle
Every argument must be backed by 2-5 sentences of original English quotes with full context.

### 2. Authentic & Objective Translation Protocol
- ❌ **Banned**: "核动力狂飙", "生死存亡之战", "降维打击"
- ✅ **Required**: Academic tone, objective, faithful to original

### 3. Linear Scaling Principle
Video越长，提取的证据越多（无上限）

---

## Troubleshooting

### "No module named 'youtube_transcript_api'"
```bash
pip3 install --break-system-packages youtube-transcript-api
```

### "No transcript found"
- The video may not have captions
- Try adding `&lang=en` to the URL
- Use a different video

### JSON serialization error
This is a known issue. Use the workaround:
```python
transcript_data = [
    {'text': item.text, 'start': item.start, 'duration': item.duration}
    for item in transcript
]
```

---

## Contributing

Contributions welcome! Please:

1. Fork this repository
2. Create a feature branch
3. Make your changes
4. Submit a Pull Request

### Areas for Improvement
- [ ] Add PDF export support
- [ ] Support more languages
- [ ] Auto-detect speaker changes
- [ ] Extract charts/visuals from video
- [ ] Integration with more AI agent platforms

---

## License

MIT — Free to use, modify, and build upon.

---

## Author

- **Original**: [@max-tutu-dev](https://github.com/max-tutu-dev)
- **OpenClaw Integration**: OpenClaw Community

---

## Acknowledgments

- Original design by [max-tutu-dev](https://github.com/max-tutu-dev)
- OpenClaw integration by the OpenClaw community
- Transcript fetching via [youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api)

---

## Related Projects

- [OpenClaw](https://github.com/openclaw/openclaw) — AI Agent Framework
- [OpenViking](https://github.com/openclaw/openviking) — Long-term memory for AI agents
- [youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api) — Transcript fetcher
