# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

## 🎬 Interview Intelligence Suite

**位置**：`~/.qclaw/workspace/skills/`

### Skills 清单

1. **video-summary** — AI 访谈视频深度摘要
   - 指南：`summary_guidelines.md`
   - 模式：V4 Dynamic Scale-to-Length Deep-Dive
   - 输出：Markdown 摘要

2. **md-to-pdf** — Markdown → 品牌化 PDF
   - 引擎：`scripts/convert_to_html.py`
   - 依赖：Python `markdown` 包 + Chrome
   - 输出：专业 PDF 报告

3. **interview-intelligence-suite** — 整体工作流
   - 主入口：`SKILL.md`
   - 集成上述两个 skills

### 快速参考

- **完整文档**：`skills/README.md`
- **快速查询**：`skills/QUICK_REF.md`
- **质量检查**：见 QUICK_REF.md 的检查清单

### 核心原则（必记）

✅ **证据优先** — 结论 = 原话 + 推理
✅ **密度放缩** — 视频越长，摘要越厚重（无上限）
✅ **翻译客观** — 忠实、字面、无演绎
✅ **数据完整** — 所有数字嵌入上下文

❌ **禁止** — 戏剧化、编辑化、标题党、压缩长视频

### 工作流

```
YouTube 视频
  ↓ [video-summary]
Markdown 摘要
  ↓ [md-to-pdf]
品牌化 PDF
```

### 命名规范

`[中文视频标题] + [核心论点摘要].pdf`

示例：`AI扩展速度超乎预期-基础设施投资合理化.pdf`

---

Add whatever helps you do your job. This is your cheat sheet.
