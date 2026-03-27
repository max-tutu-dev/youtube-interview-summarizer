# Interview Intelligence Suite

**AI 访谈深度精译系列** — 完整的视频摘要 + PDF 转换工作流

## 系统组成

### 1. video-summary Skill
**功能**：AI 访谈视频深度摘要（证据优先版）

- **输入**：YouTube URL 或转录文本
- **输出**：Markdown 摘要文件
- **核心模式**：V4 Dynamic Scale-to-Length Deep-Dive
  - 按视频时长智能扩展提取量（无上限）
  - 强制提取所有量化数据、成本、里程碑
  - 保留完整的原话逻辑链条（3-5句以上）
  - 翻译必须客观、忠实、无演绎

**关键指南**：`summary_guidelines.md`
- 证据优先（EVIDENCE FIRST）
- 问题驱动框架
- 弱信号捕捉
- 防过度压缩机制

### 2. md-to-pdf Skill
**功能**：Markdown → 品牌化 PDF 转换

- **输入**：Markdown 文件
- **输出**：专业 PDF 报告
- **自动功能**：
  - 品牌封面页（深色渐变背景）
  - 顶部彩带："AI 访谈深度精译系列"
  - 元标签：证据驱动 · 原话引用 · 精准翻译 · 客观无演绎
  - 作者卡片 + GitHub 项目卡片
  - 专业排版（Inter 字体、蓝色引用块、条纹表格）

**技术栈**：
- Python `markdown` 包 → HTML 转换
- Google Chrome 无头模式 → PDF 打印
- 自定义 CSS 主题

### 3. convert_to_html.py
**功能**：MD → HTML 转换引擎（带品牌注入）

- 自动提取视频 URL（MD 首行）
- 自动提取文档标题（第一个 H1）
- 注入品牌封面页
- 应用专业 CSS 主题

## 工作流

```
YouTube 视频
    ↓
[video-summary] 提取转录 → 按指南摘要
    ↓
Markdown 摘要文件
    ↓
[md-to-pdf] 转换 HTML → 打印 PDF
    ↓
品牌化 PDF 报告
```

## 使用示例

### 场景 1：总结 AI 访谈视频

```bash
# 1. 调用 video-summary skill
# 输入：YouTube URL 或转录文本
# 输出：AI扩展速度超乎预期-基础设施投资合理化.md

# 2. 调用 md-to-pdf skill
# 输入：上述 .md 文件
# 输出：AI扩展速度超乎预期-基础设施投资合理化.pdf
```

## 关键特性

### 证据优先协议（Evidence-First）

✅ **必须做**：
- 所有结论紧跟原话证据
- 保留完整的逻辑链条（3-5句以上）
- 提取所有量化数据、成本、里程碑
- 翻译客观、忠实、字面意思

❌ **禁止做**：
- 戏剧化词汇（"核动力狂飙"、"生死存亡"、"降维打击"）
- 编辑化、标题党、个人推断
- 只给结论不给推理过程
- 为了节省 Token 而压缩长视频

### 密度放缩原则（Uncapped Linear Scale-to-Length）

- **15 分钟视频** → 几百字摘要
- **1 小时视频** → 几千字摘要
- **2 小时视频** → 一万字以上摘要

**核心规则**：视频越长，承载的价值越多，摘要就该越厚重。绝不设置物理上限。

### 品牌化 PDF

- 深色渐变封面（蓝色系）
- 装饰圆形 + 顶部彩带
- 无页眉页脚（干净输出）
- 专业排版 + 响应式布局

## 文件结构

```
skills/
├── interview-intelligence-suite/
│   └── SKILL.md (主入口)
├── video-summary/
│   ├── SKILL.md
│   └── summary_guidelines.md
└── md-to-pdf/
    ├── SKILL.md
    └── scripts/
        └── convert_to_html.py
```

## 依赖

- Python 3 + `markdown` 包
- Google Chrome（macOS: `/Applications/Google Chrome.app`）
- YouTube 转录访问权限

## 命名规范

**输出文件命名**：`[中文视频标题] + [核心论点摘要].pdf`

示例：
- `AI扩展速度超乎预期-基础设施投资合理化.pdf`
- `大模型推理成本下降-商业化新机遇.pdf`

## 质量检查清单

在生成最终 PDF 前，验证：

- [ ] 所有数字都嵌入了上下文原话
- [ ] 每个原话块至少 3-5 句（完整逻辑链）
- [ ] 翻译是客观、忠实、无演绎的
- [ ] 提取密度与视频时长成正比
- [ ] 没有戏剧化或标题党词汇
- [ ] 封面页正确显示视频 URL 和文档标题

## 最后更新

- 2026-03-27：完成系统集成和文档编写
