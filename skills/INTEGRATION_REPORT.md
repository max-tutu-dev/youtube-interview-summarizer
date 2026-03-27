# ✅ Interview Intelligence Suite — 集成完成报告

**日期**：2026-03-27 14:25 GMT+8  
**源**：`/Users/tutuzheng/.gemini/antigravity/skills/`  
**目标**：`/Users/tutuzheng/.qclaw/workspace/skills/`

---

## 📦 集成内容

### 复制的文件

| 源文件 | 目标位置 | 状态 |
|--------|---------|------|
| `video-summary/SKILL.md` | `skills/video-summary/SKILL.md` | ✅ |
| `md-to-pdf/SKILL.md` | `skills/md-to-pdf/SKILL.md` | ✅ |
| `md-to-pdf/scripts/convert_to_html.py` | `skills/md-to-pdf/scripts/convert_to_html.py` | ✅ |
| `summary_guidelines.md` | `skills/video-summary/summary_guidelines.md` | ✅ |

### 新建的文件

| 文件 | 用途 | 行数 |
|------|------|------|
| `interview-intelligence-suite/SKILL.md` | 主入口 + 工作流说明 | 120 |
| `README.md` | 完整系统文档 | 180 |
| `QUICK_REF.md` | 快速参考卡片 | 150 |
| `TOOLS.md` (更新) | 工作区工具清单 | +60 |

**总计**：933 行代码 + 文档

---

## 🎯 系统架构

```
Interview Intelligence Suite
├── 📋 video-summary
│   ├── SKILL.md (工作流定义)
│   └── summary_guidelines.md (证据优先指南)
│       ├── 访谈类型判定
│       ├── 问题驱动框架
│       ├── V4 Dynamic Scale-to-Length Deep-Dive
│       ├── 原话证据矩阵
│       └── 翻译协议 (AUTHENTIC & OBJECTIVE)
│
├── 🎨 md-to-pdf
│   ├── SKILL.md (转换工作流)
│   └── scripts/convert_to_html.py (HTML 生成引擎)
│       ├── 品牌封面页注入
│       ├── 专业 CSS 主题
│       └── Chrome 无头打印
│
└── 🔗 interview-intelligence-suite
    └── SKILL.md (整体工作流 + 依赖管理)
```

---

## 🚀 核心能力

### 1. 证据优先摘要（Evidence-First）

✅ **强制执行**：
- 所有结论必须紧跟原话证据
- 保留完整逻辑链条（3-5 句以上）
- 提取所有量化数据、成本、里程碑
- 翻译客观、忠实、字面意思

❌ **严格禁止**：
- 戏剧化词汇（"核动力狂飙"、"生死存亡"、"降维打击"）
- 编辑化、标题党、个人推断
- 只给结论不给推理过程

### 2. 密度放缩（Uncapped Linear Scale-to-Length）

| 视频时长 | 摘要体量 | 原话块数 |
|---------|---------|---------|
| 15 分钟 | 几百字 | 5-10 |
| 1 小时 | 几千字 | 20-30 |
| 2 小时 | 一万字+ | 50+ |

**核心规则**：无上限，不压缩。视频越长，承载的价值越多，摘要就该越厚重。

### 3. 品牌化 PDF 输出

- 深色渐变封面（蓝色系）
- 顶部彩带："AI 访谈深度精译系列"
- 元标签：证据驱动 · 原话引用 · 精准翻译 · 客观无演绎
- 作者卡片 + GitHub 项目卡片
- 专业排版（Inter 字体、蓝色引用块、条纹表格）
- 无页眉页脚（干净输出）

---

## 📚 文档体系

### 主文档

1. **README.md** — 完整系统文档
   - 系统组成
   - 工作流说明
   - 关键特性
   - 依赖和配置

2. **QUICK_REF.md** — 快速参考卡片
   - 三个 Skills 的角色
   - 核心原则速查
   - 工作流速查
   - 常见问题 FAQ
   - 质量检查清单

3. **TOOLS.md** — 工作区工具清单
   - Interview Intelligence Suite 快速导航
   - 核心原则提醒
   - 工作流图示
   - 命名规范

### Skill 文档

1. **video-summary/SKILL.md**
   - 工作流定义
   - 要求和依赖
   - 验证机制
   - 交付规范

2. **md-to-pdf/SKILL.md**
   - 转换工作流
   - 依赖检查
   - HTML 生成
   - PDF 打印
   - 封面特性

3. **interview-intelligence-suite/SKILL.md**
   - 整体工作流
   - 两个 Skills 的集成
   - 使用示例
   - 依赖管理

### 指南文档

**video-summary/summary_guidelines.md** — 证据优先摘要指南
- 访谈类型判定
- 问题驱动框架
- V4 Dynamic Scale-to-Length Deep-Dive
- 原话证据矩阵规则
- 翻译协议（AUTHENTIC & OBJECTIVE TRANSLATION PROTOCOL）
- 防压缩机制
- 重点信号识别

---

## 🔧 技术栈

| 组件 | 技术 | 用途 |
|------|------|------|
| 摘要引擎 | Python + 指南 | 视频内容提取 |
| HTML 生成 | Python `markdown` 包 | MD → HTML 转换 |
| PDF 打印 | Google Chrome 无头模式 | HTML → PDF |
| 样式主题 | 自定义 CSS | 品牌化设计 |
| 字体 | Inter (Google Fonts) | 专业排版 |

---

## 📋 质量检查清单

生成 PDF 前必须验证：

- [ ] 所有数字都有上下文原话
- [ ] 每个原话块 ≥ 3-5 句（完整逻辑链）
- [ ] 翻译客观、忠实、无演绎
- [ ] 提取密度与视频时长成正比
- [ ] 没有戏剧化或标题党词汇
- [ ] 封面页正确显示视频 URL 和文档标题
- [ ] 没有页眉页脚（干净输出）
- [ ] 文件命名符合规范

---

## 🎯 使用场景

### 场景 1：总结 AI 访谈视频

```
输入：YouTube URL
  ↓ [video-summary]
输出：Markdown 摘要（几千字，完整原话块）
  ↓ [md-to-pdf]
输出：品牌化 PDF 报告
```

### 场景 2：快速参考

- **需要完整文档**？→ 读 `README.md`
- **需要快速查询**？→ 读 `QUICK_REF.md`
- **需要工作流**？→ 读 `TOOLS.md`
- **需要摘要指南**？→ 读 `summary_guidelines.md`

---

## 📍 文件位置

```
~/.qclaw/workspace/
├── skills/
│   ├── README.md ⭐ 完整文档
│   ├── QUICK_REF.md ⭐ 快速参考
│   ├── interview-intelligence-suite/
│   │   └── SKILL.md (主入口)
│   ├── video-summary/
│   │   ├── SKILL.md
│   │   └── summary_guidelines.md ⭐ 摘要指南
│   └── md-to-pdf/
│       ├── SKILL.md
│       └── scripts/convert_to_html.py
├── TOOLS.md (已更新)
└── ...
```

---

## ✨ 关键特性总结

| 特性 | 说明 |
|------|------|
| **证据优先** | 所有结论紧跟原话证据，禁止推断 |
| **密度放缩** | 视频时长 ∝ 摘要体量（无上限） |
| **翻译协议** | 客观、忠实、字面，无演绎 |
| **原话矩阵** | 3-5 句以上的完整逻辑链条 |
| **品牌化** | 深色渐变封面 + 专业排版 |
| **无压缩** | 长视频不压缩，保留所有细节 |
| **防遗漏** | 弱信号捕捉、隐含信息识别 |

---

## 🎓 学习路径

1. **快速上手**（5 分钟）
   - 读 `QUICK_REF.md`
   - 了解三个 Skills 的角色

2. **深入理解**（20 分钟）
   - 读 `README.md`
   - 理解工作流和核心原则

3. **掌握细节**（1 小时）
   - 读 `summary_guidelines.md`
   - 理解证据优先协议和翻译规则

4. **实践操作**
   - 用 video-summary 总结一个视频
   - 用 md-to-pdf 生成 PDF
   - 对照质量检查清单验证

---

## 🚀 下一步

1. **测试工作流**
   - 选择一个 AI 访谈视频
   - 调用 video-summary 生成摘要
   - 调用 md-to-pdf 生成 PDF
   - 验证输出质量

2. **优化配置**
   - 根据需要调整 CSS 主题
   - 自定义封面页信息
   - 调整翻译风格

3. **扩展功能**
   - 支持其他视频平台
   - 添加更多主题集合
   - 集成 NotebookLM 深度研究

---

## 📞 联系方式

- **作者**：Max. Zheng
- **WeChat**：18910305078
- **GitHub**：github.com/max-tutu-dev/youtube-interview-summarizer

---

**集成完成时间**：2026-03-27 14:25 GMT+8  
**状态**：✅ 就绪  
**下一步**：开始使用！
