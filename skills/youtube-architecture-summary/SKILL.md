---
name: youtube-architecture-summary
description: YouTube视频摘要引擎双端联动架构全景说明，包含系统交互时序、链路明细、核心文件索引与设计哲学
tags: [youtube, summary, architecture, documentation, antigravity, clawdbot]
author: Antigravity Team
version: 1.0.0
---

# YouTube 视频摘要引擎架构全景 (Antigravity x ClawdBot)

## 调用说明
直接调用本Skill即可查看完整架构文档，支持以下参数：
- `--diagram`：仅输出系统架构时序图
- `--files`：仅输出核心文件索引清单
- `--full`：查看完整原始架构文档

---

## 核心概览
本系统秉持**关注点分离 (Separation of Concerns)** 设计原则，将前端指挥与后端爬虫引擎彻底剥离，在不依赖任何付费第三方商业服务的前提下，实现本土化的纯血压倒性吞吐，完美应对极高频反爬与严苛排版规约。

### 核心特性
| 特性 | 说明 |
|------|------|
| 🛡️ 反爬熔断隔离 | 反爬逻辑与上层业务完全解耦，YouTube反爬算法更新仅需修改单文件 |
| ⚡ 30秒切片吞吐 | 自带IPv4强制隧道，极速绕过反爬，返回标准化30秒切片字幕流 |
| 📜 证据优先规约 | V7翻译审校总宪法强制约束大模型输出，禁止擅自归纳删减，逐句原声还原 |
| 🧱 多轨业务复用 | 架构规则通用，可快速扩展到播客摘要、会议纪要、访谈精译等场景 |
| 🎨 品牌化输出 | 自动生成暗黑极客风专业PDF报告，包含封面、元数据、统一排版 |

---

## 系统架构图
```mermaid
graph TD
    classDef user fill:#64748b,stroke:#cbd5e1,stroke-width:2px,color:#fff;
    classDef clawd fill:#1e293b,stroke:#3b82f6,stroke-width:2px,color:#fff;
    classDef antigravity fill:#0f172a,stroke:#10b981,stroke-width:2px,color:#fff;
    classDef data fill:#f8fafc,stroke:#94a3b8,stroke-width:1px,color:#334155;

    USER([👤 用户指令 / YouTube URL]):::user --> SHRIMP

    subgraph CLAWDBOT [编排终端: ClawdBot (应用业务层)]
        SHRIMP["虾总管引擎<br/>(summary-shrimp)"]:::clawd
        HTML["PDF 黑暗骑士渲染器<br/>(convert_to_html.py)"]:::clawd
        OUT[/"沉浸式硬核报告<br/>(.md / .html / .pdf)"/]:::data
    end

    subgraph ANTIGRAVITY [基建底座: Antigravity (底层武器库)]
        FETCH["原生提取探针<br/>(fetch_transcript.py)"]:::antigravity
        GUIDE["📜 V7翻译审校总宪法<br/>(summary_guidelines.md)"]:::antigravity
    end

    SHRIMP -- "① 下达提取指标" --> FETCH
    FETCH -- "② 极速绕过反爬<br>返回 30s 制式切片流" --> SHRIMP

    SHRIMP -- "③ 下达大模型总结任务" --> GUIDE
    GUIDE -- "④ 强制反制大模型浓缩<br>限定逐句原声还原" --> SHRIMP

    SHRIMP -- "⑤ 将素颜 Markdown 送入" --> HTML
    HTML -- "⑥ 加载水印与 CSS 定制" --> OUT
    OUT -.-> USER
```

---

## 核心文件索引
| 层级 | 文件名称 | 绝对路径 | 职能描述 |
|------|----------|----------|----------|
| 📐 架构层 | YouTube摘要引擎架构全景文档 | `/Users/tutuzheng/.gemini/antigravity/brain/b75e7f0e-e24e-4eb5-8e92-f9b59cf1408e/architecture_summary.md` | 本架构全局说明，包含完整设计哲学与扩展指南 |
| 🚀 业务层 | 访谈智能套件（全链路工作流） | `/Users/tutuzheng/.qclaw/workspace/skills/interview-intelligence-suite/SKILL.md` | 端到端实现：字幕提取 → 规则摘要 → PDF输出 |
| 📜 规则层 | V7翻译审校总宪法 | `/Users/tutuzheng/.qclaw/workspace/skills/video-summary/summary_guidelines.md` | 摘要生成强制规范，死盯大模型输出质量 |
| 🔧 工具层 | YouTube字幕原生提取探针 | `/Users/tutuzheng/.qclaw/workspace/fetch_youtube_transcript.py` | 带反爬能力的字幕提取工具，30秒切片输出 |

---

## 链路执行明细
### 1. 破冰层 (Data Crawling)
Antigravity提取引擎侦测到请求后，开启自带IPv4强制隧道的进程，直捣YouTube API经脉，拿到未经清洗的生肉VTT数据。随后由自带算法洗尽噪音，**产出：严格以30秒为物理单元锚定的中英纯净文本**。

### 2. 加工层 (LLM Synthesizing)
ClawdBot并未直接放任模型自由发挥，而是加载了犹如尚方宝剑的`summary_guidelines.md`。这直接抹杀了大模型的“长话短说”倾向，**产出：[保留说话人][保留等长直译][保留完整回怼] 的素颜Markdown报告**。

### 3. 交付层 (Rendering & Publishing)
最终排版器接管，打上项目的封面元数据与作者署名。**产出：包含暗黑极客风封底的`.html`与最终交付的`.pdf`**。

---

## 设计哲学
### 隔离反爬熔断风险 (Resilience)
由于反规避提取代码（`fetch_transcript`）深潜入最底层的Antigravity，如果遭遇接口封杀，只会是基座技能短暂抛出异常，而ClawdBot上层复杂的商业生成与投递业务网 毫发无损，重构极快。

### 无限制的多轨业务复用 (Modularity)
因为V7的纪律规约（`summary_guidelines.md`）是通用基座资源。如果在接下来的业务中，我们需要孵化一个名为`Podcast-Summarizer`（只做播客翻译）的新工作流，它可直接引用这份纪律资产，完全不需要我们在ClawdBot端重写一套翻译轮子。即实现了——**底层铁打的营盘，上层流水的兵**。

---

## 完整文档查看
如需查看原始完整架构文档，请执行：
```bash
cat /Users/tutuzheng/.gemini/antigravity/brain/b75e7f0e-e24e-4eb5-8e92-f9b59cf1408e/architecture_summary.md
```
