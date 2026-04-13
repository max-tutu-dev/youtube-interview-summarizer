# YouTube 视频摘要引擎 (Antigravity x ClawdBot)

一个高内聚、低耦合的双端联动YouTube视频摘要系统，具备极强的反爬能力与严苛的排版规约，实现本土化纯血压倒性吞吐。

---

## ✨ 核心特性

### 🛡️ 超强反爬能力
- 自带IPv4强制隧道，30秒切片极速绕过YouTube反爬
- 免验证码秒级提取纯净字幕，防挂起机制保障稳定性
- 反爬逻辑与上层业务完全隔离，更新仅需修改单文件

### 📜 证据优先摘要规范
- **V7翻译审校总宪法**严格约束大模型输出
- 逐句原声还原，禁止擅自归纳删减
- 保留说话人、等长直译、完整回怼
- 输出长度与视频时长线性缩放，无任意压缩

### 🎨 专业级PDF输出
- 暗黑极客风品牌化模板
- 自动生成封面、元数据、作者信息
- 清晰排版：Inter字体、蓝色块引用、条纹表格
- 无本地路径泄露，交付即成品

### 🧱 模块化架构设计
- 关注点分离，底层能力与上层业务完全解耦
- 规则、工具、编排层各司其职，无功能重叠
- 支持快速扩展到播客、会议录音等其他场景

---

## 🚀 快速开始

### 前置依赖
- Python 3.8+
- Google Chrome (macOS: `/Applications/Google Chrome.app`)
- `markdown` Python包：`pip install markdown`

### 安装
```bash
# 克隆仓库
git clone https://github.com/your-repo/youtube-summary-engine.git
cd youtube-summary-engine

# 安装依赖
pip install -r requirements.txt
```

### 使用
```bash
# 完整工作流：输入YouTube链接 → 输出Markdown摘要 → 生成PDF报告
python summarize.py https://www.youtube.com/watch?v=your-video-id

# 仅生成摘要
python summarize.py --only-md https://www.youtube.com/watch?v=your-video-id

# 本地字幕文件生成摘要
python summarize.py --transcript ./path/to/transcript.vtt
```

---

## 📁 项目结构

```
youtube-summary-engine/
├── architecture_summary.md       # 架构全景设计文档（文件6）
├── interview-intelligence-suite/ # 访谈智能套件（文件4）
│   ├── SKILL.md                  # 套件主配置
│   ├── video-summary/            # 视频摘要核心能力
│   │   ├── SKILL.md              # 摘要技能配置
│   │   └── summary_guidelines.md # V7摘要规则指南（文件3）
│   └── md-to-pdf/                # Markdown转PDF能力
│       ├── SKILL.md              # PDF转换配置
│       └── scripts/
│           └── convert_to_html.py# PDF渲染器
├── fetch_youtube_transcript.py   # YouTube字幕提取工具（文件5）
├── summarize.py                  # 统一入口脚本
└── README.md                     # 本文件
```

---

## 🏗️ 系统架构

```mermaid
graph TD
    USER([👤 用户指令 / YouTube URL]) --> SHRIMP

    subgraph CLAWDBOT [编排终端: ClawdBot (应用业务层)]
        SHRIMP["虾总管引擎<br/>(summary-shrimp)"]
        HTML["PDF 黑暗骑士渲染器<br/>(convert_to_html.py)"]
        OUT[/"沉浸式硬核报告<br/>(.md / .html / .pdf)"/]
    end

    subgraph ANTIGRAVITY [基建底座: Antigravity (底层武器库)]
        FETCH["原生提取探针<br/>(fetch_transcript.py)"]
        GUIDE["📜 V7翻译审校总宪法<br/>(summary_guidelines.md)"]
    end

    SHRIMP -- "① 下达提取指标" --> FETCH
    FETCH -- "② 极速绕过反爬<br>返回 30s 制式切片流" --> SHRIMP

    SHRIMP -- "③ 下达大模型总结任务" --> GUIDE
    GUIDE -- "④ 强制反制大模型浓缩<br>限定逐句原声还原" --> SHRIMP

    SHRIMP -- "⑤ 将素颜 Markdown 送入" --> HTML
    HTML -- "⑥ 加载水印与 CSS 定制" --> OUT
    OUT -.-> USER
```

### 层级关系
```
architecture_summary.md（架构设计）
    ↓
interview-intelligence-suite（落地实现）
    ↓
├─ summary_guidelines.md（摘要规则）
└─ fetch_youtube_transcript.py（字幕提取）
```

---

## 📊 数据流转

1. **破冰层 (Data Crawling)**：提取引擎开启IPv4隧道，直取YouTube VTT数据，清洗为30秒单元锚定的中英纯净文本
2. **加工层 (LLM Synthesizing)**：严格按照`summary_guidelines.md`生成保留完整逻辑链的素颜Markdown报告
3. **交付层 (Rendering & Publishing)**：排版器加载品牌模板，生成带封面、元数据的最终PDF报告

---

## 🎯 设计哲学

### 隔离反爬熔断风险
反规避提取代码深潜入底层基座，遭遇接口封杀时上层业务毫发无损，重构极快。

### 无限制多轨业务复用
V7纪律规约为通用基座资源，可快速扩展到播客摘要、会议纪要等新工作流，无需重写规则。

---

## 📝 输出示例

### 命名规范
`[中文视频标题] + [核心论点摘要].pdf`
示例：`AI扩展速度超乎预期-基础设施投资合理化.pdf`

### 内容结构
1. 封面页（带视频信息、元标签、作者信息）
2. 核心观点摘要
3. 分时间块完整对话翻译
4. 关键信号与数据汇总
5. 研究层延伸问题

---

## 🤝 贡献

欢迎提交Issue和PR！
- 反爬适配更新请提交到`fetch_youtube_transcript.py`
- 摘要规则调整请修改`summary_guidelines.md`
- 功能扩展请在`interview-intelligence-suite`中添加

---

## 📄 许可证

MIT License

---

## 🙏 致谢

- 摘要规则参考了NotebookLM的证据优先协议
- PDF渲染基于Headless Chrome实现
- 反爬方案集成了开源IPv4隧道技术
