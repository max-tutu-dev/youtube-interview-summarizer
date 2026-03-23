# OpenClaw Integration

This guide explains how to use the YouTube Interview Summarizer skill with **OpenClaw** — an open-source AI agent system.

---

## What is OpenClaw?

[OpenClaw](https://github.com/openclaw/openclaw) is a modular AI agent framework that supports:
- Skill-based architecture
- Multi-agent orchestration
- Long-term memory systems (OpenViking)
- Multiple channel integrations (Telegram, WeChat, Discord, etc.)

---

## Quick Start for OpenClaw Users

### Installation

1. **Clone or download this repository**

2. **Copy to OpenClaw skills directory**:
   ```bash
   cp -r youtube-interview-summarizer ~/.openclaw/skills/
   ```

3. **Verify installation**:
   ```bash
   ls ~/.openclaw/skills/youtube-interview-summarizer/
   # Should see: SKILL.md, guidelines/, examples/, etc.
   ```

### Prerequisites

**Install youtube-transcript-api**:
```bash
pip3 install --break-system-packages youtube-transcript-api
```

**Test the installation**:
```bash
python3 -c "
from youtube_transcript_api import YouTubeTranscriptApi
api = YouTubeTranscriptApi()
transcript = api.fetch('dQw4w9WgXcQ')  # Test video
print(f'✅ Fetched {len(list(transcript))} captions')
"
```

### Usage Examples

**Basic summary**:
```
总结这个访谈：https://youtu.be/rIwgZWzUKm8
```

**Full panoramic mode** (for long videos):
```
用全景模式总结这个7小时访谈：https://youtu.be/rIwgZWzUKm8
```

**Save to file**:
```
总结这个视频并保存到文件：https://youtu.be/rIwgZWzUKm8
```

---

## OpenClaw-Specific Features

### Skill Metadata

The main skill file (`SKILL.md`) includes OpenClaw-specific metadata:

```yaml
name: youtube-interview-summary
description: 深度访谈总结（证据优先、双模式输出）
version: 1.0.0
author: max-tutu-dev (adapted for OpenClaw)
tags: [youtube, video, summary, interview, research]
```

### Workflow Integration

OpenClaw agents will automatically:

1. **Read SKILL.md** to understand the workflow
2. **Follow guidelines/summary_guidelines.md** for extraction rules
3. **Use youtube-transcript-api** to fetch captions
4. **Generate structured output** following the format spec
5. **Save to projects/interviews/** by default

### Memory Integration

The skill works with OpenClaw's memory systems:
- **OpenViking**: Stores interview insights as semantic memories
- **Daily logs**: Auto-saves summaries to `memory/YYYY-MM-DD.md`
- **QMD**: Indexes summaries for semantic search

---

## File Structure (OpenClaw Layout)

```
~/.openclaw/skills/youtube-interview-summary/
├── SKILL.md                      # Main skill definition
├── QUICKSTART.md                 # Quick start guide
├── TESTING.md                    # Testing instructions
├── OPENCLAW_INTEGRATION.md       # This file
├── guidelines/
│   └── summary_guidelines.md     # Extraction rules
├── examples/
│   └── sample_output.md          # Example summary
└── skills/
    └── video-summary/
        └── SKILL.md              # Original Antigravity skill
```

---

## Customization for OpenClaw

### Change Output Directory

Edit `SKILL.md` → "Default Output Paths" section:

```yaml
output:
  interviews: ~/clawd/projects/interviews/
  transcripts: /tmp/
```

### Add More Channels

OpenClaw supports multi-channel delivery. Add to `SKILL.md`:

```yaml
delivery:
  channels:
    - wechat
    - telegram
    - discord
```

### Integrate with Other Skills

**Combine with Memos**:
```
总结这个访谈，然后把核心观点保存到Memos：[URL]
```

**Convert to PPT**:
```
总结这个访谈，然后生成PPT：[URL]
```

**Add to IMA Knowledge Base**:
```
总结这个访谈，然后上传到IMA知识库：[URL]
```

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

### "JSON serialization error"
This is a known issue with `youtube-transcript-api`. The skill includes a workaround:

```python
transcript_data = [
    {
        'text': item.text,
        'start': item.start,
        'duration': item.duration
    }
    for item in transcript
]
```

---

## Example OpenClaw Session

```
User: 总结这个访谈：https://youtu.be/rIwgZWzUKm8

Agent: 好的！让我总结这个YouTube访谈...

[Fetching transcript...]
✅ 成功获取 13,171 条字幕
视频时长: 404.5 分钟

[Generating summary...]
模式选择: 模式2 - 全景时间戳复盘（长视频）

报告生成中...
✅ 完成！文件已保存到: ~/clawd/projects/interviews/saining-xie-7hr-report.md

📊 报告统计:
- 9个章节
- 30+个证据块
- 8000+字

需要我把报告发送到其他平台吗？（微信、Telegram、IMA知识库等）
```

---

## Contributing

If you improve the OpenClaw integration, please:

1. Fork this repository
2. Create a branch: `git checkout -b openclaw-improvements`
3. Commit your changes
4. Push to your fork
5. Create a Pull Request

---

## License

MIT — Same as the original YouTube Interview Summarizer project.

---

## Author

- **Original**: [@max-tutu-dev](https://github.com/max-tutu-dev)
- **OpenClaw Adaptation**: OpenClaw Community

---

## Related Projects

- [OpenClaw](https://github.com/openclaw/openclaw) — AI Agent Framework
- [youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api) — Transcript fetcher
- [OpenViking](https://github.com/openclaw/openviking) — Long-term memory system
