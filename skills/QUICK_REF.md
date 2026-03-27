# 快速参考 — Interview Intelligence Suite

## 三个 Skills 的角色

| Skill | 功能 | 输入 | 输出 |
|-------|------|------|------|
| **video-summary** | 视频深度摘要 | YouTube URL / 转录文本 | Markdown 摘要 |
| **md-to-pdf** | Markdown → PDF | .md 文件 | 品牌化 PDF |
| **interview-intelligence-suite** | 整体工作流 | 视频 | PDF 报告 |

## 核心原则（必读）

### 1️⃣ 证据优先（Evidence First）
- 结论 = 原话 + 推理
- 禁止无根据的推断
- 保留完整逻辑链（3-5句以上）

### 2️⃣ 密度放缩（Scale-to-Length）
- 15 分钟 → 几百字
- 1 小时 → 几千字
- 2 小时 → 一万字+
- **无上限**，不压缩

### 3️⃣ 翻译协议（Authentic & Objective）
- ✅ 客观、忠实、字面
- ❌ 戏剧化、编辑化、标题党
- 匹配说话人的原始语调

### 4️⃣ 数据提取（Key Signals）
- 所有数字、成本、里程碑
- 嵌入上下文原话中
- 不单独列"数字清单"

## 工作流速查

```
Step 1: 获取转录
  → YouTube 视频 / 转录文本

Step 2: 调用 video-summary
  → 按 summary_guidelines.md 摘要
  → 输出：[标题].md

Step 3: 调用 md-to-pdf
  → 转换 HTML + 注入品牌
  → 输出：[标题].pdf
```

## 文件位置

```
~/.qclaw/workspace/skills/
├── README.md (完整文档)
├── QUICK_REF.md (本文件)
├── video-summary/
│   ├── SKILL.md
│   └── summary_guidelines.md ⭐ 摘要指南
├── md-to-pdf/
│   ├── SKILL.md
│   └── scripts/convert_to_html.py
└── interview-intelligence-suite/
    └── SKILL.md (主入口)
```

## 常见问题

**Q: 视频很长（2小时+），怎么办？**
A: 不要压缩！按 V4 Dynamic Scale-to-Length 原则，输出应该是一万字以上的详细报告。

**Q: 翻译时能加入个人观点吗？**
A: 不能。必须客观、忠实、字面。说话人是数据驱动的分析师，输出应该读起来像严肃的分析报告。

**Q: 原话块要多长？**
A: 最少 3-5 句话，包含完整的逻辑链条（推理过程）。不能只给结论。

**Q: PDF 封面能自定义吗？**
A: 可以。编辑 `convert_to_html.py` 中的 CSS 和 HTML 模板。

**Q: 支持其他视频平台吗？**
A: 目前针对 YouTube 优化。其他平台需要先获取转录文本。

## 质量检查清单

生成 PDF 前必须验证：

- [ ] 所有数字都有上下文
- [ ] 每个原话块 ≥ 3-5 句
- [ ] 翻译客观无演绎
- [ ] 提取密度 ∝ 视频时长
- [ ] 无戏剧化词汇
- [ ] 封面 URL 和标题正确

## 命名规范

```
[中文视频标题] + [核心论点摘要].pdf

示例：
✅ AI扩展速度超乎预期-基础设施投资合理化.pdf
✅ 大模型推理成本下降-商业化新机遇.pdf
❌ 视频摘要.pdf (太通用)
❌ Interview_Summary_2026.pdf (无中文标题)
```

## 技术栈

- **语言**：Python 3
- **MD 处理**：`markdown` 包
- **HTML 生成**：自定义 Python 脚本
- **PDF 打印**：Google Chrome 无头模式
- **字体**：Inter (Google Fonts)
- **主题**：深色渐变 + 蓝色系

## 联系方式

- **作者**：Max. Zheng
- **WeChat**：18910305078
- **GitHub**：github.com/max-tutu-dev/youtube-interview-summarizer

---

**最后更新**：2026-03-27
