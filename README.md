# 🎬 YouTube访谈视频智能摘要系统
> 证据优先·逐句原声还原·零信息损耗·品牌化PDF输出
> 
> 全链路自动化工作流：YouTube链接 → 字幕提取 → AI深度摘要 → 专业PDF报告

---
## ✨ 核心特性
### 🎯 证据优先协议（V7翻译审校总宪法）
✅ **100%原声还原**：逐句提取原文，禁止大模型擅自归纳、删减、演绎
✅ **零信息损耗**：所有数字、时间、专有名词完整保留上下文
✅ **客观中立**：翻译忠实字面含义，不添加主观解读
✅ **动态长度适配**：视频越长，摘要越厚重，无压缩上限

### 🚀 技术优势
- 🔑 **原生字幕提取**：自带IPv4强制隧道，30秒切片极速绕过反爬
- 🧠 **双大模型架构**：推理+翻译分离，保证专业领域准确性
- 🎨 **暗黑极客风PDF**：自动生成带封面、元数据、专业排版的品牌化报告
- 📦 **开箱即用**：一条命令/一个Skill调用完成全链路处理

---
## 📁 项目结构
```
youtube-interview-summarizer/
├── 📖 README.md                          # 项目说明文档（本文件）
├── .gitignore                            # Git忽略配置
├── 📦 skills/                            # 核心Skill模块
│   ├── interview-intelligence-suite/     # 全链路工作流入口
│   │   ├── SKILL.md                      # 技能配置说明
│   │   ├── README.md                     # 套件详细文档
│   │   └── summarize.py                  # 一键调用脚本
│   ├── video-summary/                    # 视频摘要核心能力
│   │   ├── SKILL.md                      # 技能配置说明
│   │   └── summary_guidelines.md         # V7摘要生成强制规范
│   ├── md-to-pdf/                        # Markdown转PDF工具
│   │   ├── SKILL.md                      # 技能配置说明
│   │   └── scripts/
│   │       └── convert_to_html.py        # PDF渲染引擎
│   └── youtube-architecture-summary/     # 系统架构说明
│       └── SKILL.md                      # 架构文档入口
└── 🛠️ tools/
    └── fetch_youtube_transcript.py       # YouTube字幕提取工具
```

---
## 🚀 快速开始
### 方式1：Skill调用（推荐）
在OpenClaw中直接调用全链路工作流：
```
/skill interview-intelligence-suite https://www.youtube.com/watch?v=xxx
```

### 方式2：命令行使用
```bash
# 完整链路：YouTube链接 → 摘要 → PDF
python3 skills/interview-intelligence-suite/summarize.py https://www.youtube.com/watch?v=xxx

# 只生成Markdown摘要
python3 skills/interview-intelligence-suite/summarize.py https://www.youtube.com/watch?v=xxx --only-md

# 本地Markdown转PDF
python3 skills/interview-intelligence-suite/summarize.py ./summary.md --only-pdf

# 指定输出目录
python3 skills/interview-intelligence-suite/summarize.py https://www.youtube.com/watch?v=xxx -o ./output
```

---
## 📚 核心文档索引
| 文档名称 | 路径 | 说明 |
|----------|------|------|
| 🔹 系统架构全景说明 | `/skills/youtube-architecture-summary/SKILL.md` | 双端联动架构、交互时序、设计哲学 |
| 🔹 V7摘要生成规范 | `/skills/video-summary/summary_guidelines.md` | 摘要生成强制遵守的核心规则 |
| 🔹 全链路工作流说明 | `/skills/interview-intelligence-suite/README.md` | 套件详细使用指南、参数说明 |
| 🔹 PDF样式配置说明 | `/skills/md-to-pdf/SKILL.md` | PDF模板自定义、样式调整说明 |

---
## 🎨 输出示例
### 生成的PDF报告包含：
1. 专业暗黑风格封面（视频标题、时长、发布日期）
2. 摘要元数据（生成时间、核心标签、观点数量统计）
3. 分章节结构化摘要（按演讲主题自动分段）
4. 关键信息高亮（数字、时间、重要结论自动标注）
5. 完整原声引用（所有结论都标注原文出处）

---
## 🤝 贡献指南
欢迎提交Issue和PR！
- 功能建议：请先描述使用场景和需求
- Bug反馈：请附上错误日志和输入链接
- 代码贡献：请遵循现有代码风格和架构设计

---
## 📄 许可证
MIT License
