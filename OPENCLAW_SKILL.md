---
name: youtube-interview-summary
description: |
  深度YouTube访谈视频总结技能，专为长篇技术/商业/投资访谈设计。

  当用户要求总结YouTube访谈视频、提取演讲要点、分析访谈内容时使用此技能。

  核心特性：
  - 证据优先：每个论点附带英文原话（2-5句上下文）
  - 双模式输出：短视频（核心论点） vs 长视频（全景时间戳回放）
  - 严格翻译协议：客观、学术、忠实原文，拒绝渲染
  - 智能扩容：视频越长，提取证据越多（无上限线性放缩）

  适用于：技术访谈、商业对话、投资分析、行业专家分享等深度内容。

homepage: https://github.com/max-tutu-dev/youtube-interview-summarizer
metadata:
  openclaw:
    emoji: 🎥
    requires:
      env: []
      tools: []
    capabilities:
      - web_search
      - file_write
    primaryEnv: null
---

# YouTube Interview Summary

> 原话是证据，翻译只是透镜。

专为AI Agent设计的YouTube访谈视频深度总结工具，将数小时的访谈转化为结构化、可验证的智能报告。

## 核心原则

### 证据优先 (Evidence-First)
- 每个论点必须附带2-5句英文原话
- 保留完整上下文，不截取零散短句
- 禁止推断或补充外部信息

### 翻译协议 (STRICT)
- **禁用词汇**: "核动力狂飙"、"生死存亡之战"、"降维打击"
- **要求**: 学术、客观、忠实、数据驱动
- **语气**: 与说话者保持一致（分析师→分析式，工程师→技术式）

## 使用方式

### 基础用法

```
用户: 总结这个YouTube访谈 https://youtube.com/watch?v=xxx
```

**工作流程**:
1. 获取视频字幕（使用youtube-transcript或网页抓取）
2. 判断视频长度 → 选择模式
3. 提取核心论点/章节拆解
4. 生成结构化报告

### 模式选择

| 视频长度 | 推荐模式 | 输出特点 |
|---------|---------|---------|
| < 1小时 | 模式1：核心论点驱动 | 3-5个论点，每个2-3段证据 |
| > 1小时 | 模式2：全景时间戳复盘 | 按章节拆解，10-20个证据块 |

### 输出格式

```markdown
# [中文标题]

## 访谈对象洞察
- 背景与立场分析
- "屁股位置"（利益相关）

## 硬核信号与数据
- 所有量化事实
- 金额、规模、里程碑

## 逻辑层
- 模式1: 3-5个核心论点
- 模式2: 按时间戳章节回放

### 📌 证据块示例
**📌 语境**: 解释这段话的背景

**🗣️ 原话**:
> [3-5句英文原话]

**🇨🇳 翻译**:
客观、学术的中文翻译

## 研究层
- NotebookLM深度追问清单
```

## 文件结构

```
youtube-interview-summary/
├── SKILL.md                  # 本文件（主技能入口）
├── README.md                 # 项目说明
├── guidelines/
│   └── summary_guidelines.md # 完整指导方针（必读）
├── examples/
│   └── sample_output.md      # 示例输出
└── skills/
    └── video-summary/
        └── SKILL.md          # 原始工作流文件
```

## 详细指导

完整的提取规则、翻译协议和输出格式规范请参考：
`guidelines/summary_guidelines.md`

**关键章节**:
- 工作流与结构
- 模式1 vs 模式2的触发条件
- 🔥 AUTHENTIC & OBJECTIVE TRANSLATION PROTOCOL
- 防压缩机制（避免AI"偷懒"）

## 示例输出

查看真实案例：
`examples/sample_output.md` (Dylan Patel 2.5小时AI基础设施访谈)

## 注意事项

1. **长视频警告**: 处理>1小时视频时，输出文件会非常大（可能10000+字），使用`write`工具直接写入文件，不要在对话中输出
2. **字幕获取**: 需要youtube-transcript或类似工具支持
3. **PDF导出**: 可选，需要md-to-pdf工具
4. **质量检查**: 生成前必须验证：
   - 证据密度是否充足
   - 翻译是否符合协议
   - 是否保留了所有关键数字

## 许可证

MIT License - 原作者 max-tutu-dev
