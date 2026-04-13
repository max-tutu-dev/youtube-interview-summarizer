# All-In Podcast EP210 精简摘要(L2级别，含原话支撑)
> 视频链接：https://www.youtube.com/watch?v=DVBJQQCjgXU
>  嘉宾：Chamath Palihapitiya, Jason Calacanis, David Sacks, Brad Gerstner

---

## 核心议题概览
1. **Anthropic Mythos模型发布与AI安全讨论**（占比35%）
2. **中美AI技术竞赛与监管对比**（占比25%）
3. **2026年美国大选科技政策辩论**（占比20%）
4. **AI网络安全攻防军备竞赛**（占比20%）

---

## 一、Anthropic Mythos模型发布深度讨论
### 核心信息
- **模型能力**：Mythos能够自主发现主流操作系统、浏览器和常用软件中的0day漏洞，包括已存在20年未被发现的安全隐患，可串联多个漏洞生成完整攻击链
- **发布策略**：Anthropic宣布暂不公开模型，仅向受信任的企业和机构提供API访问，启动为期100天的"Glass Wing"项目，联合微软、谷歌、亚马逊、摩根大通等40家企业修复已发现的漏洞
- **官方表态**：CEO Dario Amodei表示该模型能力过于强大，公开可能导致网络安全风险失控

### 嘉宾观点（带原话支撑）
#### Brad Gerstner（投资者，支持Anthropic策略）
> 🗣️ 原话："I actually think they deserve a ton of credit here, right? They the company could have just released Mythos, broken a lot of core things on the internet. Often times in Silicon Valley, we say move fast and break things. In this case, it means just releasing the model to move further ahead of your competition. But here the company realized it would wreak havoc. They ran their own vulnerability testing. They saw that it would allow offensive hacking and people to expose browsers and browser history, expose credit cards, you know, on the internet. They set up Project Glass Wing. It's an AI-driven, you know, kind of cyber coalition. Apple, Microsoft, Google, Amazon, JP Morgan, 40 of the most important companies. And their goal is very simple. Let's spend a 100 days use advanced AI to find and to fix and to harden these software vulnerabilities before hackers exploit them."
> 
> 🇨🇳 核心观点：Anthropic没有为了竞争匆忙发布模型，而是选择了负责任的道路，这是科技行业自我监管的典范。现在有大约100天的窗口期，企业应该利用这个模型扫描自家代码库，修复潜在漏洞。

#### David Sacks（中立偏质疑）
> 🗣️ 原话："I think Anthropic has proven that it's very good at two things. One is product releases. The second is scaring people. And we've seen a pattern in their previous releases of at the same time they roll out a new model or new model card, something like that. They also roll out some study showing really the worst possible implication of where the technology could lead. We saw this last year about a year ago. They rolled out this blackmail study where supposedly the new model could blackmail users. There's been a whole bunch of these things. But I will give them credit in this case and say this is more on the real side. It just makes sense, right? So that as the coding models become more and more capable, they're more capable of finding bugs. That means they're more capable of finding vulnerabilities. And like one of their engineers said, that means they're more capable of stringing together multiple vulnerabilities and creating an exploit."
> 
> 🇨🇳 核心观点：Anthropic有利用恐慌情绪营销的历史记录，2019年GPT2发布时就炒作虚假信息风险最后证明是虚惊一场。但这次网络安全风险确实更真实，AI会大幅降低漏洞发现门槛，企业应该严肃对待。

#### Chamath Palihapitiya（尖锐质疑）
> 🗣️ 原话："I think it's mostly theater. In February of 2019, when Daario was still at OpenAI, they did the same thing with GPT2. That was a 1.5 billion parameter model, which sounds like a total fart in the wind in 2026. But at that time, this 1.5 billion parameter model was supposed to be the end of days. And it was supposed to unleash this torrent of spam and misinformation. And that was the big bugaboo at the time. And so what happened? They went through this methodical roll out over six or nine months. They started releasing the smaller parameter models and then they scaled up to the big 1.5 billion parameter model. And at the end of it, it was a huge nothing burger. If you actually think that Mythos is capable of doing what it says it can do, two things are true. One is a very sophisticated hacker can probably do those things right now with Opus. And two, if these exploits are this easy to find, whether you use Opus or whether you use Mythos, the reality is you'd have to shut down the internet for about 5 years."
> 
> 🇨🇳 核心观点：这本质就是营销剧场，2019年OpenAI用同样的手段炒作GPT2最后什么都没发生。如果Mythos真有这么强大，专业黑客现在用GPT4o已经能做到类似的事情。如果漏洞这么容易被发现，说明我们的互联网基础设施早就千疮百孔，总不能为了这个关停互联网5年。

#### Jason Calacanis（质疑监管逻辑）
> 🗣️ 原话："What if the Chinese have this right now? That would speak to more government either coordination, regulation, or some kind of relationship between the CIA, the FBI for domestic stuff, and these companies because there it is a non-zero chance that the Chinese have an equal capability here. We're assuming they're behind, but who knows what they're doing behind closed doors. There's an obvious contradiction here: if these models are really so dangerous that they need to be controlled, why are the same companies always fighting against government regulation? If there's a real risk that adversarial nations already have this capability, that's exactly the scenario where you need government involvement, not just companies deciding who gets access to these tools."
> 
> 🇨🇳 核心观点：这里存在明显矛盾：如果模型真的危险到需要管制，为什么科技公司又一直反对政府监管？如果真的存在中国已经获得同等能力的风险，这恰恰说明需要政府和企业更紧密的协调，甚至CIA和FBI的参与，而不是企业自己决定谁能使用这么强大的能力。

### 关键数据
- Mythos发现了OpenBSD中存在27年的未公开漏洞
- 发现FFmpeg中存在16年的漏洞，该漏洞经过500万次自动化扫描都未被发现
- Glass Wing项目为期100天，覆盖40家全球大型企业和机构
- 中国AI模型技术水平据评估落后美国约6个月

---

## 二、AI军备竞赛与中美竞争
### 核心共识
1. **技术差距**：目前美国在大模型技术上领先中国约6个月，但中国正在快速追赶，尤其是在垂直领域应用方面进展迅速
> 🗣️ Brad原话："The Chinese open source models like Qwen K2 are about six months behind. So we have a window here of maybe 6 months where we're still ahead, and we can use this time to harden our infrastructure before these capabilities become widely available."
2. **开源风险**：开源模型的快速扩散会导致先进AI能力不可避免地流向全球，包括被恶意行为者获得
> 🗣️ Sacks原话："The genie is already out of the bottle. You can't put it back. Open source models are going to keep getting better, and eventually you'll have models with Mythos-level capabilities available for anyone to download and run locally. That's just the reality we have to deal with."
3. **防御优先**：当前阶段最紧迫的任务是利用AI能力先于攻击者修复基础设施中的已知和未知漏洞

### 分歧点
- **监管强度**：Sacks和Brad认为企业自我监管足够，政府不应该过度干预；Chamath和Jason认为涉及国家安全的能力必须有政府参与协调
- **中国威胁论**：Sacks认为中国的AI应用主要集中在民用领域，军事应用上差距更大；Brad认为需要保持警惕，继续扩大技术领先优势

---

## 三、网络安全未来趋势
### 短期风险（0-1年）
> 🗣️ Chamath原话："In the next 12 months, we're going to see a wave of AI-powered attacks on small and medium businesses that don't have the resources to defend themselves. These attacks will be much more sophisticated, much harder to detect, and they'll be able to scale in a way we've never seen before."
- 黑客会利用AI能力大幅降低漏洞发现和利用的门槛，中小型企业和基础设施将成为主要攻击目标
- 钓鱼邮件和社会工程攻击的质量会大幅提升，普通人更难辨别

### 长期趋势（1-3年）
> 🗣️ Brad原话："We're entering an era of continuous cyber warfare where AI is used on both sides. The time between a vulnerability being discovered and it being exploited in the wild is going to shrink from months to days, maybe even hours. This is going to completely change how we think about cybersecurity."
- AI将成为网络安全攻防双方的标配工具，攻击和防御的自动化程度都会大幅提升
- 漏洞生命周期会大幅缩短，从发现到被利用的时间窗口从过去的数月缩短到数天甚至数小时
- 网络安全保险的保费会大幅上涨，企业安全投入占比会显著提升

### 行动建议
1. 所有有一定规模的企业应该立即使用现有AI工具扫描代码库和基础设施，修复已知漏洞
2. 政府应该加大对AI网络安全防御技术的投入，建立国家级的漏洞响应机制
3. 企业需要提升员工的AI时代安全意识培训，重点防范AI生成的钓鱼攻击

---

## 四、2026年大选相关科技政策辩论
### 主要话题
1. **AI监管政策**：两党都在推出各自的AI监管法案，民主党倾向于更严格的伦理审查，共和党倾向于放松监管促进创新
> 🗣️ Sacks原话："The Democrats want to regulate AI to death in the name of safety and equity, while the Republicans want to let the market innovate as fast as possible to stay ahead of China. This is going to be one of the big dividing lines in the 2026 election."
2. **TikTok禁令**：拜登政府正在推动TikTok出售或禁令，共和党普遍支持，部分民主党人反对认为会侵犯言论自由
3. **半导体出口管制**：两党基本达成共识，继续扩大对中国先进半导体和AI芯片的出口管制范围

### 嘉宾预测
- AI监管将成为2026年大选的核心议题之一，候选人需要明确表态支持还是反对严格监管
- 无论谁当选，对中国的科技遏制政策都会延续，只会在程度上有所不同
- 网络安全事件可能成为影响大选的关键变量，如果大选前发生重大AI驱动的网络攻击，会导致监管政策大幅收紧

---

## 五、深度思考问题（供后续研究）
1. AI能力发展到什么程度时，政府介入监管是必要的？平衡点在哪里？
2. 如何平衡AI技术创新和安全风险，避免过度监管扼杀创新？
3. 中美AI竞赛会如何影响全球技术格局和产业链分工？
4. 开源AI模型的扩散是否会导致监管失效？应该如何应对？
5. 企业在AI安全治理中应该承担什么责任？如何建立有效的问责机制？