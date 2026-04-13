https://www.youtube.com/watch?v=bTA8sjgvA4c
# 谷歌AI演进历程与未来展望 - Sundar Pichai深度访谈

---

## 访谈基本信息
- **视频标题**：The history and future of AI at Google, with Sundar Pichai
- **视频URL**：https://www.youtube.com/watch?v=bTA8sjgvA4c
- **时长**：70分钟
- **受访者**：Sundar Pichai（谷歌/Alphabet CEO，任职第10年）
- **摘要规范**：V7翻译审校总宪法 · 全景时间轴完整问答还原版

---

### 1. 访谈对象洞察（立场背景/屁股位置）

**Sundar Pichai**：谷歌（现为Alphabet）首席执行官，刚刚度过担任CEO的第十个年头。他于2004年加入谷歌，最初管理Chrome浏览器和谷歌工具栏等项目。2015年成为谷歌CEO，2019年起担任Alphabet CEO。

**立场分析**：
- **利益代言**：作为谷歌CEO，Pichai必须向投资者和公众展示谷歌在AI竞赛中的领导地位，特别是在Transformer架构起源于谷歌、但产品化被OpenAI先行的背景下
- **双重压力**：既要承认谷歌在商业化上落后于ChatGPT的事实，又要强调谷歌在基础研究、基础设施（TPU）和垂直整合方面的长期优势
- **战略辩护**：在视频中，Pichai需要在多个层面为谷歌辩护：1) Transformer研究成果的商业化路径 2) AI竞赛中的长期战略 3) 大规模资本投入（2026年1750亿美元CapEx）的合理性
- **风格特征**：典型的工程师式思考 - 强调数据、基础设施、系统性优势，避免夸大或戏剧化表述

---

### 2. 硬核信号与数据（Key Signals & Data）

| 信号类别       | 具体内容                                                                 |
|----------------|--------------------------------------------------------------------------|
| **资本规模**   | 2026年谷歌计划投入1750-1850亿美元资本支出                               |
| **历史节点**   | Transformer架构诞生于谷歌（2017年），但ChatGPT先于谷歌产品化              |
| **产品指标**   | 过去五年搜索延迟改善了30%，团队有毫秒级的延迟预算考核机制                |
| **投资组合**   | 谷歌持有SpaceX约10%股份、Anthropic约10%股份，Waymo占多数股权             |
| **市场数据**   | Stripe每年处理1.9万亿美元全球支付，占全球GDP的1.6%                        |
| **技术指标**   | Gemini Flash模型能力达到Pro模型的90%，但响应速度显著更快                 |
| **业务规划**   | Wing无人机配送服务计划覆盖4000万美国人口                                  |
| **前沿布局**   | 首次提到量子计算数据中心在太空的概念                                      |
| **开源动态**   | Gemma 4开源模型基于Gemini 3架构，权重文件可放入U盘                        |
| **安全变化**   | AI导致的零日漏洞黑市价格正在下降                                          |
| **组织管理**   | Pichai每周花费1小时进行细粒度的TPU资源分配决策                            |
| **技术扩散**   | 2027年将成为AI在企业非工程流程中应用的关键转折点                          |
| **内部代号**   | 谷歌内部代理系统Antigravity的代号是Jet Ski                                |
| **投资逻辑**   | 长期项目按5-10年时间维度评估期权价值和潜在市场规模                        |
| **资源约束**   | 内存、晶圆产能、建设许可是AI行业当前最核心的物理约束                      |
| **决策机制**   | 长期项目决策基于底层技术进展曲线而非短期商业回报                          |
| **创新模式**   | 太空数据中心等前沿项目最初仅由少数人团队启动，预算规模很小                |
| **转型挑战**   | 大型企业AI转型的最大障碍是组织变革管理和权限体系重构                      |

---

### 3. V7 全景时间轴完整问答还原版

#### [00:00 - 03:39] 开场：Transformer的起源与商业化悖论
> **核心议题**：谷歌在Transformer架构上的开创性研究为何未能率先推出ChatGPT式产品

---

**[采访者]**：
> "Sundar Pichai just passed a decade as CEO of Google. Alphabet is now not only one of the world's biggest tech companies, but a leader in the AI race, with plans to spend $175 billion in CapEx in 2026. Cheers. A bit of history that people talk about a lot in the context of Google and AI is the fact that Transformers were invented at Google, but then productized outside of Google with mostly ChatGPT and that style of product. How do you reflect on that now?"

**🇨🇳 精译**：Sundar Pichai刚刚度过了担任谷歌CEO的第十个年头。Alphabet现在不仅是世界上最大的科技公司之一，也是AI竞赛的领导者，2026年计划投入1750亿美元资本支出。干杯。在谷歌和AI的背景下，人们经常谈论的一段历史是Transformer是在谷歌发明的，但后来主要被ChatGPT等产品在谷歌外部实现了商业化。你现在如何反思这件事？

---

**[Sundar Pichai]**：
> "I think it's actually worth talking about. It's a bit misunderstood. Transformers was done in the context of a lot of TPUs, Transformers were all done to solve a specific product need to some extent. The team is thinking about how to make translation better. In the case of TPUs, how do you… Hey, speech rec works, but you suddenly have to sell it to two billion people. We don't have enough chips for it. How do you solve inference for it? I hadn't known that. Transformers were specifically— It was from our research teams, but they were guided by solving product problems."

**🇨🇳 精译**：我认为这个问题值得深入讨论。人们对这个情况有些误解。Transformer架构是在大量TPU背景下开发的，在一定程度上都是为了解决特定产品需求。团队在思考如何让翻译更好。在TPU的情况下，语音识别是有效的，但突然需要向二十亿用户提供服务时，芯片就不够了。如何解决推理问题？我以前不知道的是，Transformer特别针对我们的研究团队，但他们的工作都受到解决产品问题的指导。

---

**[Sundar Pichai]**：
> "Transformers were immediately used. BERT and MUM, people underestimate how much, because we measure search quality so religiously. Some of the biggest jumps in search quality in that period where search went ahead of everyone else was because of BERT and MUM. We built Transformers and used it immediately in Search to improve language understanding, understanding web pages, understanding your queries, kept building better models. We also started productizing it internally in the form of, there were teams building something called LaMDA. Obviously, we weren't the first to ship that. But I think it's less to do with it was just research, and we weren't applying it in a product direction. That, I think, is just— You did this research, you then saw massive ROI from using it the way you intended, and then you didn't invent all of the products that were invented with it, but that's to be expected. I would go a step further. We exactly even conceived the product, which is ChatGPT. It was LaMDA. If you remember, there was an engineer inside who thought it was sentient. Think of it as an early version of ChatGPT he was speaking to, internally."

**🇨🇳 精译**：Transformer立即被投入使用。BERT和MUM，人们低估了它们的影响程度，因为我们极其认真地在衡量搜索质量。在那个搜索领先于所有其他竞争对手的时期，一些最大的搜索质量跳跃正是由于BERT和MUM。我们构建了Transformer并立即在搜索中使用它来改善语言理解、理解网页、理解查询，并持续构建更好的模型。我们也开始在内部以团队形式产品化它，有团队正在构建一个叫做LaMDA的东西。显然，我们不是第一个发布它的。但我认为这更多与不仅仅是研究有关，我们并非没有在产品方向上应用它。我想这更多是——你做了这项研究，然后看到了按预期方式使用它带来的巨大投资回报率，然后你并没有发明用这项技术发明的所有产品，但这是可以预料的。我会更进一步。我们实际上甚至构想出了产品，这就是ChatGPT。它就是LaMDA。如果你还记得，公司内部有一位工程师认为它有感知能力。把它想象成他正在对话的早期ChatGPT版本，内部版本。

---

**[Sundar Pichai]**：
> "We even had the product version of it in the multiverse, somewhere else. Google probably shipped that nine months later or something like that. In fact, in the Google I/O in '22, we launched something called AI Test Kitchen, and that was LaMDA, but we had constrained it because internally, we didn't have an end-to-end version which was RLHF-ed. The version I saw was a lot more toxic at a level. We couldn't have possibly put it out at that time."

**🇨🇳 精译**：我们甚至在其他地方、另一个宇宙中拥有它的产品版本。谷歌大概在九个月后才发布了它。事实上，在2022年Google I/O大会上，我们推出了一个叫做AI Test Kitchen的东西，那就是LaMDA，但我们限制了它，因为在内部，我们没有经过RLHF（人类反馈强化学习）的端到端版本。我看到的那个版本在某种程度上有害得多。我们当时不可能发布它。

---

#### [03:39 - 07:41] 速度作为战略差异化因素
> **核心议题**：谷歌如何将速度（延迟）作为核心产品战略
> **阶段硬核信号**：搜索延迟五年改善30%，团队有毫秒级延迟预算考核机制

---

**[采访者]**：
> "Also, I think as a company, which had this search quality bias, we had a higher bar, maybe, for what we thought was an acceptable product quality to go out. But it wasn't like… We were figuring out how to get it out. I would also argue that even when OpenAI shipped, they did their deal with Microsoft probably a couple of months before. You can look back and say it wasn't entirely fully obvious. I think they were lucky to also see it on the coding side with GitHub. I think maybe there was a signal we were missing."

**🇨🇳 精译**：此外，我认为作为一家具有这种搜索质量偏见的公司，我们对于什么样的产品质量可以推出有更高的标准，也许。但这并非说…我们正在想办法把它推出来。我也认为，即使OpenAI发布产品时，他们可能与微软的协议是在几个月前达成的。你可以回顾并说这并不完全明显。我认为他们很幸运地在GitHub的编程方面也看到了这一点。我想也许我们错过了一个信号。

---

**[采访者]**：
> "Coding side, probably, you were seeing more of a sequential jump than probably just on the language side. Maybe the jumps between GPT-2 and 3 and later 4 were more pronounced if you were using it for coding, too. You can point to things. I think to answer your original question, I think it was less that research-to-product than a bunch of other factors. I remember talking to some of the people who worked on ChatGPT, and I think they launched it the week of Thanksgiving. It was a little bit of a buried launch. It wasn't like, this is a big, prominent thing, and this is going to be an important part of our future. It was clearly a surprise. I think it was a cool test case. It was really interesting. But the way I internalize these moments is if you're in consumer internet, you're going to have surprises."

**🇨🇳 精译**：编程方面，你可能看到的是更多的连续跳跃，而不仅仅是语言方面。也许GPT-2到GPT-3以及后来GPT-4之间的跳跃，如果你把它用于编码，也会更加明显。你可以指出这些事情。我认为要回答你的原始问题，这更多的不是研究到产品的问题，而是一系列其他因素。我记得和一些在ChatGPT工作过的人交谈过，我认为他们在感恩节那一周发布了它。这是一个有点被埋没的发布。它并不像，这是一个很大、很突出的事情，这将成为我们未来重要的一部分。这显然是一个惊喜。我认为这是一个很酷的测试案例。真的很有趣。但我理解这些时刻的方式是，如果你在消费互联网领域，你会遇到惊喜。

---

**[采访者]**：
> "We were at Google when, Elad and I, there was something called Google Video Search. YouTube came out. Just that we acquired YouTube. Or think about if you were in Facebook, Instagram came out. Nobody sits and says… You don't look at those moments with that drama because Facebook just bought Instagram. But the way I've internalized is consumer internet, 3 people are going to be sitting and prototyping and throwing out millions of things. I'm not trying to diminish anything, but I'm just saying you're always going to have these moments. I don't think people wake up in a garage and ship a better iPhone. That's not going to happen. But that's not how consumer internet is. You just have to be conscious of that and to internalize that."

**🇨🇳 精译**：当我和Elad在谷歌时，有一个叫做Google Video Search的东西。YouTube出现了。我们收购了YouTube。或者想想，如果你在Facebook，Instagram出现了。没有人会坐着说…你不会用那种戏剧性的方式看待那些时刻，因为Facebook直接收购了Instagram。但我理解的方式是，在消费互联网领域，总会有三四个人坐在那里，制作原型，推出数以百万计的东西。我不是想贬低任何事情，我只是说你总是会遇到这些时刻。我不认为有人会在车库里醒来就推出更好的iPhone。这不会发生。但这并不是消费互联网的运作方式。你只需要意识到这一点并理解这一点。

---

**[采访者]**：
> "As I think about the AI race in 2026, one thing that strikes me is Google has for so long had speed as the place it tries to differentiate. Original Google Search was really fast and famously displayed the search query time within the results, sort of showing off. Then Gmail Fast Search compared to the competitors of the time, or Chrome, compared to the competitors of the time. And now, I use all of the AI services for different things, but Gemini on TPUs is just so fast. I'm curious how much this is part of the explicit product strategy and how you think of it, or it's much more nuanced than that."

**🇨🇳 精译**：当我思考2026年AI竞赛时，让我印象深刻的是，谷歌长期以来一直把速度作为试图区分自己的地方。最初的谷歌搜索真的很快，并著名地在结果中显示搜索查询时间，有点像炫耀。然后Gmail的快速搜索与当时的竞争对手相比，或者Chrome与当时的竞争对手相比。而现在，我为不同的事情使用所有AI服务，但TPU上的Gemini就是这么快。我很好奇这在多大程度上是明确产品战略的一部分，以及你如何看待它，或者这比那要微妙得多。

---

**[Sundar Pichai]**：
> "I've always internalized speed. Let's call it latency for this purpose, and as one of the distinguishing features of a great product. Also, it almost always reflects the technical underpinnings of the product having been done well. There's a different speed which matters, too, which is the speed of shipping and iteration and release cycles. Both are important. But you talk about latency. It's easy to say you want latency, but you're constantly adding capabilities. The capability frontier is progressing."

**🇨🇳 精译**：我一直把速度内化。让我们称之为延迟，以此目的，并作为优秀产品的区分特征之一。而且，它几乎总是反映了产品技术基础做得很好。还有另一种速度也很重要，那就是发布速度和迭代以及发布周期。两者都很重要。但你谈论的是延迟。说你想减少延迟很容易，但你不断地增加能力。能力前沿正在进步。

---

**[Sundar Pichai]**：
> "There's some sense of, how do you balance that? That's where it gets more complicated. But to give an example, like Search, I was speaking with the teams. They now have for sub-teams, latency budgets in the milliseconds. You get 50% credit... If you ship something which shaves off 3 milliseconds, you earn 1.5 milliseconds for your latency budget, and 1.5 milliseconds gets passed on to the user. Depending on what we think you're doing, some people may get a latency budget of 30 milliseconds or 10 milliseconds. You can use it, but you have rigorous reviews against that. But that's how much we think it matters. For context, I guess humans pick it up in the low hundreds of milliseconds, is that correct? In terms of where it actually impacts?"

**🇨🇳 精译**：某种程度上，你如何平衡这一点？这就是事情变得更复杂的地方。但举个例子，比如搜索，我和团队交谈过。他们现在对于子团队有毫秒级的延迟预算。你获得50%的信用…如果你发布了削减3毫秒的东西，你为你的延迟预算获得1.5毫秒，1.5毫秒传递给用户。根据我们认为你在做什么，有些人可能获得30毫秒或10毫秒的延迟预算。你可以使用它，但你有严格的审查机制。但我们就是这么重视它。作为背景，我猜人类在大约一两百毫秒内就能察觉到，对吗？就它实际影响的地方来说？

---

**[Sundar Pichai]**：
> "That's right. I think we've actually, last I checked the dashboard and the metrics, we've actually improved Search latency by 30% in the last five years. But think about the functionality progression that's happened. This is why in Gemini, we deeply think about that parade of frontier of making sure the capability to speed, and the flash models are at like 90% the capability of the pro models, but much faster, much more effective to serve, and the vertical integration helps and so on."

**🇨🇳 精译**：没错。我认为我们实际上，我上次检查仪表盘和指标时，我们在过去五年里实际上改善了搜索延迟30%。但要想想发生的功能进展。这就是为什么在Gemini中，我们深入思考那个前沿游行，确保能力与速度相匹配，而闪存模型大约有专业模型90%的能力，但响应速度显著更快，服务效率高得多，垂直整合也有帮助，等等。

---

#### [07:41 - 13:38] 搜索的未来与Agentic变革
> **核心议题**：搜索是否会演变成Agentic系统，以及AI如何重塑信息获取方式
> **阶段硬核信号**：Stripe每年处理1.9万亿美元支付，占全球GDP1.6%，2025年谷歌股价约150美元

---

**[采访者]**：
> "How do you think about the future of Search, actually? Because a lot of people now are talking about chat as a new interface. Obviously, Gemini is incorporated, or Search has incorporated Gemini or AI results in the context of Google. But a lot of people are not talking about agentic flows, and everybody's going to have a personal agent who, instead of typing in a query, it'll go and do something for you. Instead of asking about trips, it'll go and plan a trip for you. What do you view as the future of Search? Is it a distribution mechanism? Is it a future product? Is it one-of-N ways people are going to interact with the world?"

**🇨🇳 精译**：实际上，你如何看待搜索的未来？因为现在很多人都在谈论聊天作为一种新界面。显然，Gemini已经被整合进来，或者搜索已经整合了Gemini或AI结果，在谷歌的背景下。但很多人没有谈论代理流程，每个人都将拥有一个个人代理，它不是输入查询，而是为你做一些事情。不是询问旅行，而是为你规划旅行。你如何看待搜索的未来？它是一个分发机制吗？它是一个未来的产品吗？它是人们与世界互动的N种方式之一吗？

---

**[Sundar Pichai]**：
> "I feel like in Search, with every shift, you're able to do more with it. We have to absorb those new capabilities and keep evolving the product frontier. If it's mobile, the product evolved pretty quickly. You're getting out of a New York subway, you aren't looking for web pages, you want to go somewhere, how do you find it? You're constantly shifting… People's expectations shift and you're moving along. If I fast-forward, a lot of what are just information-seeking queries will be agentic in Search. You'll be completing tasks. You'll have many threads running. Will Search exists in 10 years? Well, you may— Or just evolves into something? It keeps evolving. Search would be an agent manager in which you're doing a lot of things."

**🇨🇳 精译**：我感觉在搜索中，随着每次转变，你能够用它做更多事情。我们必须吸收这些新能力，并不断推进产品前沿。如果是移动端，产品演进得相当快。当你走出纽约地铁时，你不是在寻找网页，而是想去某个地方，你怎么找到它？你不断地转变…人们的期望在转变，你也在随之移动。如果我快进，很多仅仅是信息寻求的查询将会在搜索中变成代理式的。你将完成任务。你将运行许多线程。搜索还会存在10年吗？嗯，你可能会…或者只是演变成某种东西？它不断进化。搜索将成为一个代理管理器，你会在其中做很多事情。

---

**[Sundar Pichai]**：
> "I think in some ways, I use Antigravity today, and you have a bunch of agents doing stuff. I can see search doing versions of those things, and you're getting a bunch of stuff done. I think the root of your question is, if you think of Search as a prompt that is not longer than one line, returning a bunch of different ranked results, as opposed to just telling you the right answer or something. I think your question is, does that product modality exist? But today in AI mode in Search, people do deep research queries. That doesn't quite fit the definition of what you're saying. But people adapted to that. I think people will do long-running tasks. Yes. It can be asynchronous."

**🇨🇳 精译**：我认为在某种程度上，我今天使用Antigravity，你有一堆代理在做事情。我可以看到搜索在做这些事情的版本，你完成了一堆事情。我认为你问题的根源是，如果你把搜索看作是一个不超过一行的提示，返回一系列不同的排名结果，而不是仅仅告诉你正确的答案或什么的。我认为你的问题是，那种产品形态是否存在？但今天在搜索的AI模式下，人们进行深入研究查询。这不完全符合你所说的定义。但人们已经适应了这一点。我认为人们会进行长时间运行的任务。是的。它可以是异步的。

---

#### [13:38 - 19:40] 战略反思：投资者误解与AGI思考
> **核心议题**：投资者为何在2025年低估谷歌AI实力，以及谷歌对AGI的真实态度
> **阶段硬核信号**：谷歌2016年宣布TPU，CapEx从300亿增至约1800亿美元，谷歌内部代号Jet Ski即Antigravity

---

**[采访者]**：
> "When we talk about Search and where it's going and things like this, I'm reminded of the fact that basically a year ago, spring/summer of '25, sentiment was very negative on Google. The prevailing view was that Search is cooked, and we're going to have a really hard time. The core business model is under attack, blah, blah, blah. Google was trading for $150-ish a share. Now people have realized that's silly. Google has up and down the stack, whether it be applications or models or TPUs or whatever—as well as Waymo and YouTube and all the cool bets. What do you think investors, as a proxy for informed sentiment, misunderstood this time last year?"

**🇨🇳 精译**：当我们谈论搜索及其发展方向以及这些事情时，我想起了一个事实，那就是大约一年前，2025年春夏，市场情绪对谷歌非常负面。主流观点是搜索已经玩完了，我们将面临非常困难的时期。核心商业模式受到攻击，等等。谷歌股价大约在150美元左右。现在人们意识到这是愚蠢的。谷歌在全栈上下都有布局，无论是应用程序、模型还是TPU等等——还有Waymo、YouTube以及所有很酷的投资。你认为投资者，作为知情情绪的代表，去年这个时候误解了什么？

---

**[Sundar Pichai]**：
> "Because clearly, there was some big misunderstanding. It was obviously very invert-focused in that moment. To me, it was very clear in that moment, 'Hey, the Overton window shifted.' I felt like the company was built for that moment. The vertical thing, it's not an accident or something. It was a very intentful… We were in the seventh version of TPUs. I remember it might have been 2016 Google I/O where we announced the TPUs and spoke about we are building AI data centers. This was 2016. We were thinking about… The company was operating in an AI-first way. We had deeply internalized this shift. To me, we were behind in terms of frontier LLM models, but we had all the capabilities internally, and we had to execute to meet the moment. But the exciting part was when I look at it from a full stack, we had the research teams, we had the infrastructure teams, we had all the platforms. We had been investing intentfully in many businesses. To me, I suddenly felt like, 'Wow, we have this one common technology which can accelerate all those businesses.' Search to YouTube to Cloud to Waymo all relies on progress. It was a very leveraged way to make progress. I understood it. To the earlier point of the discussion, I didn't view it as a zero-sum moment at all."

**🇨🇳 精译**：因为很明显，当时存在一些重大误解。显然在那个时刻市场非常聚焦于反转观点。对我来说，那个时刻非常清楚，"嘿，奥弗顿窗口移动了。"我觉得公司就是为那个时刻而建的。垂直整合这件事，它不是偶然或什么。这是非常刻意的…我们当时处于TPU的第七个版本。我记得可能是2016年Google I/O，我们宣布了TPU并谈论我们正在构建AI数据中心。那是2016年。我们当时在思考…公司正以AI优先的方式运营。我们已深深内化了这种转变。对我来说，在前沿LLM模型方面我们落后了，但我们在内部拥有所有能力，我们必须执行以满足这个时刻。但令人兴奋的部分是，当我从全栈视角看时，我们拥有研究团队，我们拥有基础设施团队，我们拥有所有平台。我们一直有意识地在许多业务上进行投资。对我来说，我突然觉得，"哇，我们拥有这个共同的技术，它可以加速所有这些业务。"从搜索到YouTube到云到Waymo都依赖于进步。这是一个非常有杠杆效应的进步方式。我理解了这一点。回到讨论的早期点，我根本不认为这是一个零和时刻。

---

**[采访者]**：
> "My first feeling the AGI moment was 2012 when Jeff Dean demoed the earliest version of Google Brain. This is when the neural networks recognized a cat. That was 2012. I went with Larry to the DARPA Challenge. It might have been 2014, I think. I need to be exact about when we went there, seeing the cars drive there. Demis demoing the earliest versions of the models, having what we would call as imagination. There have been many moments like that, so it was obvious that technology is progressing. In terms of living now and having a visceral feel for it, I think the closest, I would say, is if you're coding, and you give it a complex task, and you never open the ID, and you're in some agent manager world, and you see it do it, and how powerful it is. You can call it feel the AGI. There are moments like that. I did a little hobby project recently, and after a while, I was like, 'Oh, I wonder what language it's using?' That was a detail that I needed to ask it about after everything was up and running. It feels like magic. Moments like that for sure. The slope of the curve is what surprises you. You're improving it on so many paradigms. It feels clear that there's going to be progress ahead."

**🇨🇳 精译**：我第一次感受到AGI时刻是在2012年，当Jeff Dean演示了Google Brain的最早版本。那是神经网络识别猫的时候。那是2012年。我和Larry一起参加了DARPA挑战赛。可能是2014年，我想。我需要准确记住我们什么时候去的，看到汽车在那里行驶。Demis演示了最早的模型版本，拥有我们称之为想象力的东西。有很多这样的时刻，所以很明显技术正在进步。就现在生活并有切身体验而言，我认为最接近的是，如果你在编码，你给它一个复杂的任务，你从不打开IDE，你在某种代理管理器世界中，你看到它完成任务，以及它有多强大。你可以称之为感受AGI。有这样的时刻。我最近做了一个小小的爱好项目，过了一会儿，我想，"哦，我想知道它在使用什么语言？"这是一个在所有事情都启动并运行后我需要问它的细节。感觉很神奇。肯定有这样的时刻。曲线的斜率让你惊讶。你在这么多范式上改进它。很明显未来会有进步。

---

#### [19:40 - 29:55] 行业约束与硬件战略
> **核心议题**：AI行业面临的物理瓶颈，以及谷歌的硬件战略调整
> **阶段硬核信号**：内存是短期关键约束，Gemma 4模型权重可放入U盘，Wing服务计划覆盖4000万美国人

---

**[采访者]**：
> "Look, at some level, you have to work back to actual wafer capacity or something like that. There are deeper ground truths. I think so, wafer starts. It's a fundamental constraint. I think power and energy are more solvable. Permitting and actually working through a regulatory environment might be a constraint. The pace at which you can do things. Even though there's lots of land in pro-growth, Texas or Nevada or Montana, just maybe not enough. I think we're making tremendous progress. I think for the US, I think it's a particularly important thing. You're in awe of the pace in China, how fast they can build things. I really think we need to learn to build things much faster. You almost have to shift your mentality to think about what would it take to do things 10X faster in the physical world, construct 10X faster. I would worry about that as a constraint. I think there could be growing resistance, so it's not as simple as a few people deciding we want to build fast. The data-center moratoriums and stuff. I would say wafer starts, the ability to permit and do things. I do think there's a lot of good work being done from the government on."

**🇨🇳 精译**：在某些层面上，你必须追溯到实际的晶圆产能或类似的东西。有更深层次的基本事实。我认为是晶圆开工。这是一个基本约束。我认为电力和能源更容易解决。许可和实际通过监管环境可能是一个约束。你做事情的速度。尽管在支持增长的德克萨斯、内华达或蒙大拿有很多土地，但可能还不够。我认为我们正在取得巨大进展。我认为对美国来说，这是一件特别重要的事情。你对中国建设速度感到敬畏，他们能多么快地建造东西。我真的认为我们需要学会更快地建造东西。你几乎必须转变心态，思考在物理世界中做事情10倍更快需要什么，建造10倍更快。我会担心这是一个约束。我认为可能会有越来越多的阻力，所以这不仅仅是几个人决定我们想要快速建造的问题。数据中心的暂停和类似的事情。我会说是晶圆开工，许可能力和做事能力。我认为政府正在做很多好的工作。

---

#### [29:55 - 43:48] 前沿技术布局与长期愿景
> **核心议题**：谷歌在量子计算、太空数据中心等前沿领域的长期布局
> **阶段硬核信号**：量子计算可能模拟天气和现实，太空数据中心处于最早阶段

---

**[Sundar Pichai]**：
> "At abstract level, to me, it feels like to simulate nature more and more. Given it's inherently quantum, you would need quantum systems to better simulate it. We may get there with classical computing techniques in a surprising way or get at it with enough compression. Abstraction, it may work, but I fundamentally felt like Quantum would have an edge there. I don't know, we still don't understand the Haber process for fertilizer. There are many complex… It's probably your background going back to what you did in college, more. My instinct tells me there'll be simulating weather, simulating reality, all that, I think, Quantum will have an advantage. History of technology is you get something to a scale where it works, and then you use it and people's creativity on the top finds the application. I always give this example of mobile phones plus GPS enabled Uber. There's nobody who is working on phones who would predict that as an outcome of this platform shift. I'm confident quantum will have many, many applications if you can actually make it work. That's how I think about it."

**🇨🇳 精译**：在抽象层面上，对我来说，感觉是越来越多地模拟自然。鉴于它在本质上是量子的，你会需要量子系统来更好地模拟它。我们可能通过经典计算技术以令人惊讶的方式到达那里，或者通过足够的压缩达到它。抽象化，它可能奏效，但我从根本上感觉量子在那里会有优势。我不知道，我们仍然不理解肥料哈柏过程。有很多复杂的…这很可能和你大学时期所学背景有关。我的直觉告诉我，量子在模拟天气、模拟现实等所有方面都会有优势。技术的历史是，你把某种东西发展到可行的规模，然后你使用它，人们在此基础上发挥创造力找到应用。我总是以手机加上GPS促成优步为例。没有一个从事手机工作的人会预测到这个作为平台转变的结果。如果你真的能让它工作，我相信量子将会有许多许多应用。我就是这么想的。

---

**[采访者]**：
> "We actually think about the question you were asking Elad a bit ago about what are those longer-term things. Thinking at that stage, it's easier because your initial funding amounts can be smaller. But then you stay committed for the long term, but you're making sure you're making progress in a deep way. As long as you're seeing that underlying tech... Take Quantum, for example. How do we judge it? We're judging the underlying... You have goals around what logical qubit error, correct, a large stable logical qubit threshold by when you're going to get to, and is the team able to do that? I think you assess it that way. One of the, I wouldn't say advantages... I think one of the ways we have thought about it and we've been disciplined about, or at least to me, matters a lot, is to make those early technology bets in a deep way. That's helped. On a constant basis, look, I've always viewed it as you have to assess the long-term value of these things. It's almost like in some intuitive way, you're thinking about the option value and the TAM of something 5–10 years down the line, and you assume a crazy growth and think through whether those decisions make sense."

**🇨🇳 精译**：我们实际上在思考你之前问Elad的关于那些长期事情是什么的问题。在那个阶段思考更容易，因为你的初始资金可以少一些。但随后你会长期投入，但要确保你在深入地取得进展。只要你看到底层技术…以量子为例。我们如何判断它？我们在判断底层…你有关于逻辑量子比特误差的目标，在什么时候你能达到一个大的稳定逻辑量子比特阈值，团队是否能够做到这一点？我认为你用这种方式评估。我不会说这是优势…我认为我们思考这个问题的方式之一，我们一直很自律，或者至少对我来说非常重要的是，深入地进行早期技术押注。这很有帮助。持续地看，我一直认为你必须评估这些东西的长期价值。几乎是以某种直觉的方式，你在思考5-10年后某个东西的期权价值和潜在市场规模，你假设一个疯狂的增长，然后思考这些决策是否合理。

---

**[Sundar Pichai]**：
> "The TPU investments have been great that way. We've steadily invested in that. Waymo was a great example where I think we increased our investment two to three years ago when the rest of the world got pessimistic on it. When others, some of the people were backing off. It's very magical. It's such a magical experience. I take Waymo now every day to work when I can. I think Waymo is a good example of this question I have, which is Google does cut projects, and there's various things you've tried where you said, 'We're actually not going to fund this part of X all the way, or we're going to retire this product. It's not working.' But Waymo, despite the fact that it was a long road from a compelling demo to commercial service in market, you guys didn't lose the faith. What was it that you were seeing? Is that a qualitative decision or a quantitative decision? How do you decide that we're going to cut Loon but keep Waymo?"

**🇨🇳 精译**：TPU投资在这方面做得很好。我们一直在稳步投资。Waymo是一个很好的例子，我认为我们在两三年前当世界其他地方对它感到悲观时增加了投资。当其他人，一些人在退缩时。这非常神奇。这是一个非常神奇的体验。我现在只要可以就每天坐Waymo去上班。我认为Waymo是我有这个问题的一个很好的例子，谷歌确实会砍掉项目，你尝试过各种事情，你会说，"我们实际上不会一直资助X的这部分，或者我们要停用这个产品。它不起作用。"但Waymo，尽管从令人信服的演示到市场上的商业服务还有很长的路要走，你们并没有失去信心。你看到了什么？这是定性决策还是定量决策？你如何决定我们要砍掉Loon但保留Waymo？

---

**[Sundar Pichai]**：
> "I think it's to do with that, some quantified… You look at the Waymo driver. That's the underlying technology, which how does the software drive the car? The progress in terms of safety and reliability. It's a long-running task, how safe and how will you do it. You follow that curve, and you predict, or you set goals where you want to be and how you perform against those curves. I think the team has been phenomenal. There have been maybe phases where it didn't progress, but those are the times you need to… You have confidence in the quality of the team to break through those phases. I think the more you're able to evaluate things at that deeper technology level, I think you tend to make those decisions better, or at least that's how I have tried to do it."

**🇨🇳 精译**：我认为这与一些量化的东西有关…你看看Waymo的驾驶系统。这是底层技术，软件如何驾驶汽车？在安全性和可靠性方面的进展。这是一项长期的任务，有多安全以及你会怎么做。你跟踪那个曲线，你预测，或者你设定目标，你想要达到什么位置，以及你如何对照这些曲线执行。我认为团队非常出色。可能有些阶段没有取得进展，但那些时候你需要…你对团队的质量有信心，他们能突破这些阶段。我认为你越能够在更深的技术层面评估事物，你往往会做出更好的决策，或者至少这是我努力去做的方式。

---

#### [43:48 - 56:22] 资本分配与组织管理
> **核心议题**：谷歌如何在不同性质的项目间分配资本，以及AI对组织管理的影响
> **阶段硬核信号**：TPU预算分配每周需要Pichai专门思考一小时，谷歌内部代理系统代号Jet Ski

---

**[采访者]**：
> "One argument I've heard or one discussion I've heard made about Waymo is that a lot of the huge gains that have been seen recently... Because it used to be this hand-mapped heuristics of how do you deal with the edge cases of driving or something happens, how do you respond? A subset of those were almost like hand-drawn out for the cars to follow. It had a narrow set of things that it could do. Then really, the breakthrough was moving to end-to-end deep learning a couple of years ago as this big Transformer wave was happening in general. Do you think if Waymo had been started five years ago, it'd be at the same place as it is relative to having been started 15 plus years ago? Just given that that's the breakthrough that's propelled it forward."

**🇨🇳 精译**：我听到关于Waymo的一个论点或讨论是，最近看到的很多巨大进步…因为过去是手工映射的启发式方法，来处理驾驶的边缘情况或发生某事时如何响应？其中一部分几乎像是为汽车手工绘制的规则。它能做的事情范围很窄。然后真正的突破是在几年前转向端到端深度学习，当时整个行业正经历Transformer大潮。你认为如果Waymo是五年前开始的，它会和15多年前开始的现在处于同一位置吗？考虑到这是推动它前进的突破。

---

**[Sundar Pichai]**：
> "Look, I think we spoke earlier about robotics. You can think about Waymo as a robot. I think people who are starting robotics in the last three years, by definition, will be making faster progress, maybe. But I think Waymo is such an integrated system. There are aspects of it, not quite like you take something complex like TSMC or SpaceX launching things. You are talking about system integration in these things in a very complex way. I think Waymo has hidden aspects of that, which the time of how you do it, the craft of it matters. But having said that, I do think the end-to-end approaches are going to be an accident in this case. Because just having a team, arguably, was a huge benefit to Alphabet and Google. Just the fact that you kept investing in it, and then it hit a moment in time where this technology lift-off was more than worth it, and was very smart and forward-thinking. I just think it's interesting to ask, how does that apply to other domains? Because to your point on robotics, it seems like with robotics, we'll potentially have a different history where you can move very quickly now."

**🇨🇳 精译**：我想我们之前谈到过机器人技术。你可以把Waymo看作一个机器人。我认为在过去三年里开始机器人项目的人，从定义上说，可能会取得更快的进展。但我认为Waymo是一个如此集成的系统。它有一些方面，不太像你拿台积电或SpaceX发射东西这样复杂的东西来比。你在谈论这些东西的系统集成，方式非常复杂。我认为Waymo有隐藏的方面，你怎么做的时间，工艺很重要。但话虽如此，我确实认为端到端方法在这种情况下会是一个意外。因为仅仅拥有一个团队，可以说对Alphabet和谷歌来说是一个巨大的好处。你持续投资它，然后它遇到了一个时刻，这项技术的起飞非常值得，这非常聪明和有远见。我只是认为问这个问题很有趣，这如何适用于其他领域？因为正如你关于机器人的观点，似乎对于机器人，我们可能会有不同的历史，现在你可以非常快地前进。

---

**[采访者]**：
> "Do you folks think about re-internalizing hardware again, or is it largely going to be a partner-driven model to bringing this stuff to the world? I think we'd keep a very open mind. My lesson from Waymo and on the AI side with TPUs, et cetera, I need to really push the curve well, particularly in areas where you have safety, regulatory, everything. You want the first-hand experience of the product feedback cycle. I think having first-party hardware will end up being very important. That's how I would say right at this stage."

**🇨🇳 精译**：你们是否考虑过重新将硬件内部化，或者很大程度上会是合作伙伴驱动的模式来将这些东西推向市场？我认为我们会保持非常开放的心态。我从Waymo和AI方面的TPU等得到的教训是，我需要很好地推动曲线，特别是在你有安全、监管等所有问题的领域。你想要产品反馈周期的第一手经验。我认为拥有第一方硬件最终会非常重要。这就是我在现阶段的看法。

---

**[采访者]**：
> "Sorry, I have two more capital allocation questions. Can you make the case that Google has historically been under-levered, where Google has historically carried a strong net cash position? Given that both Google has more ideas than it knows what to do with, it's just brimming with good ideas, and just the core business grows very durably, and I think Google clearly has a very good understanding of that core business, and it has grown at a higher rate than Google's cost of capital. As you look back on it, should Google have been more leaned in and said, 'Okay, we will be willing to have a leveraged position that's slightly more aggressive than strong unit cash, and we will put that towards new initiatives, or just buy more of this core Google business for Google shareholders, or do more minority investing, which again, Google seems to have been best in class at?'"

**🇨🇳 精译**：抱歉，我还有两个资本分配问题。你能说明谷歌历史上杠杆率不足的情况吗，谷歌历史上一直持有强劲的净现金头寸？鉴于谷歌有太多想法都不知道该做什么，充满了好主意，核心业务增长非常持久，我认为谷歌显然对核心业务有很好的理解，而且它的增长率高于谷歌的资本成本。当你回顾过去时，谷歌是否应该更积极地说，"好吧，我们愿意持有比强劲单位现金略激进的杠杆头寸，我们将把它用于新的举措，或者为谷歌股东回购更多的核心谷歌业务，或者做更多的少数股权投资，谷歌在这方面似乎一直是一流的？"

---

**[Sundar Pichai]**：
> "It's a great question. For example, if Waymo had reached this point earlier, I think I would have invested the capital earlier. To some extent, I think you were judging it by... You want to be good stewards of capital. To the extent you're bullish on ROIC, you want to invest every last dollar you can there. But to the extent you have excess where you don't think... This is why we've invested in other companies, too, even if not in. But we always thought about it with the lens of being good stewards of it. We felt our investment in Stripe was being a good steward of our capital. SpaceX, and Anthropic and so on. I think now with the AI shift, there are more opportunities on which we can deploy capital in a good way, and so we are doing that. I think we always had that mindset. I would have been glad to invest more capital in Waymo earlier, but we weren't at the level of maturity needed to do that. There was a point in Waymo, from a safety standpoint, we did approach Waymo safety first, and it wasn't the right thing to do. You feel like you cannot point to projects where they would have gone faster had they gone more capital sooner? They had a natural ramp."

**🇨🇳 精译**：这是一个很好的问题。例如，如果Waymo更早达到这一点，我想我会更早投资资本。在某种程度上，我认为你是通过…来判断的。你想成为资本的好管家。只要你对投资回报率持乐观态度，你就想在那里投入每一分钱。但如果你有过剩的资金而你不认为…这就是为什么我们也投资了其他公司，即使不是内部项目。但我们一直以成为好管家的视角来考虑这个问题。我们觉得我们对Stripe的投资是对我们资本的良好管理。SpaceX、Anthropic等等。我认为现在随着AI的转变，有更多的机会我们可以很好地配置资本，所以我们正在这样做。我认为我们一直有这种心态。我本来很乐意更早地在Waymo投入更多资本，但我们还没有达到这样做所需的成熟度。在Waymo的某个阶段，从安全角度来看，我们确实把安全放在首位，当时投入更多资本并不是正确的做法。你觉得你不能指出那些如果更早投入更多资本会进展更快的项目吗？它们有自然的增长曲线。

---

**[采访者]**：
> "I would say that, but I think in generally, at least, we might have gotten the decision wrong, but our approach, at least, was to say, if you got excited about something and had the conviction, you were willing to commit the capital to see it through. Another capital allocation question was, historically at tech companies, the large majority of the R&D expense was the people walking around the building. Headcount was managed through a very tightly-controlled process. Indeed, as you thought about allocating R&D effort, it was really allocating highly-paid people to go work on the challenge. The tech costs were, unless you were doing something very computationally expensive, which obviously Google did in place of Google Books or something. Broadly speaking, the tech was an afterthought compared to the cost of the people. We're now going to a world where, as you say, that's not the case with TPUs and how you allocate that. Just at a very concrete budgeting level, how does that work inside of Google? Do you have an overall TPU budget for the company? Then, when you are giving a project resourcing, previously you gave it a certain headcount budget, and now you give it a headcount and a TPU budget. Are they the same budget? Just how does that work when you're doing a quarterly review or an annual review?"

**🇨🇳 精译**：我会这么说，但我认为总的来说，至少，我们可能做出了错误的决定，但我们的方法至少是说，如果你对某件事感到兴奋并有信心，你愿意投入资本来完成它。另一个资本分配问题是，历史上在科技公司，大部分研发费用是在大楼里走动的人员。人员编制通过一个非常严格控制的流程来管理。实际上，当你考虑分配研发工作时，实际上是分配高薪人员去应对挑战。技术成本，除非你在做计算量非常大的事情，显然谷歌在谷歌图书之类的项目上是这样。广义上讲，与人员成本相比，技术是事后考虑的。我们现在进入了一个世界，正如你所说，TPU和你如何分配它的情况并非如此。只是在非常具体的预算层面，谷歌内部是如何运作的？你有公司整体的TPU预算吗？然后，当你给一个项目分配资源时，以前你给它一定的人员预算，现在你给它人员和TPU预算。它们是同一个预算吗？当你进行季度审查或年度审查时，这是如何运作的？

---

**[Sundar Pichai]**：
> "Look, we've always had a compute budget. Asking for a friend. Now, we've always had a compute budget, even in classic compute. I would say with ML, and we use both TPUs and GPUs, by the way, extensively. ML compute planning is... We are super thoughtful about headcount planning, too, but we have always had to plan that. ML compute, we've gone through phases where they've been easy, and then there have been phases where we've been constrained as a company. But now it is really acutely constrained. You spend a lot more time. I at least spend a dedicated hour a week thinking about that question at a pretty granular level. I will know by projects and by teams, the compute units they are using, or at least I have that information, and I'm looking at it and assessing it. In some ways, it's a really important thing to be doing right now, I feel."

**🇨🇳 精译**：我们一直有计算预算。帮朋友问问。现在，我们一直有计算预算，即使在传统计算中也是如此。我会说在机器学习方面，顺便说一下，我们广泛使用TPU和GPU。机器学习计算规划是…我们对人员规划也非常深思熟虑，但我们一直必须规划。机器学习计算，我们经历了一些阶段，那时候计算资源很容易获得，然后还有一些阶段我们作为公司受到了约束。但现在真的非常紧张。你花费更多时间。我每周至少专门花一个小时思考这个问题，在相当细粒度的层面上。我会按项目和团队来了解他们正在使用的计算单元，或者至少我有这些信息，我在查看它并评估它。在某种程度上，我认为现在做这件事真的很重要。

---

#### [56:22 - 70:00] 未来展望：AI普及与组织变革
> **核心议题**：AI如何改变企业工作流，以及技术扩散面临的挑战
> **阶段硬核信号**：2027年将成为AI企业应用关键转折点，太空数据中心项目仅由少数人启动

---

**[采访者]**：
> "The scarce resource is compute in a lot of cases, and so you're ensuring that Google's precious compute resources are being spent on the most worthwhile— That's right. Initiatives. How do you think about that in the context of GCP and Google Cloud? Because there you're actually allocating the compute to others instead of for your own purposes and given the constraints in the system, how do you think through that differential allocation? Look, we plan ahead. When we do the forward planning, the Cloud team is forward planning, and they are putting a plan in place. You're funding that, and you're doing that for our internal needs. You forward plan. As part of that, you're also signing long-term commitments to customers. Anything we commit to a customer is sacrosanct. These are contractual commitments. You solve a lot of it with planning. When you plan, we're all in a constrained world. I think the Cloud team would say they don't have the computer they want, et cetera. But you solve it with planning ahead."

**🇨🇳 精译**：在很多情况下，稀缺资源是计算能力，所以你要确保谷歌宝贵的计算资源被用在最有价值的——没错。项目上。在GCP和谷歌云的背景下，你如何看待这一点？因为在那里你实际上是在将计算能力分配给其他人，而不是用于你自己的目的，考虑到系统中的限制，你如何考虑这种差异化分配？我们提前规划。当我们进行前瞻性规划时，云团队会进行前瞻性规划，他们会制定计划。你为其提供资金，你这样做也是为了我们的内部需求。你提前规划。作为其中的一部分，你也会与客户签订长期承诺。我们对客户做出的任何承诺都是神圣不可侵犯的。这些是合同承诺。你可以通过规划解决很多问题。当你规划时，我们都处于一个受限的世界里。我认为云团队会说他们没有想要的计算能力，等等。但你可以通过提前规划来解决。

---

**[采访者]**：
> "Speaking of Google Cloud, I have my product request that I've been saving up for this section that I know you're looking forward to. You could have posted it on X. Exactly. But no, I'll say one thing that works really well is the GCP/MCP is awesome, where your AI can just interact programmatically with Google Cloud. I guess you guys have exposed almost everything except the core permission stuff. I feel like In a way, part of the curse of Google Cloud has been there is so much functionality there that I'm sure you occasionally hear from people. It was a little hard to navigate that you log in, you have to create an organization, a project, and whatever, and find the right services, whatever. Now, all that doesn't matter. You just say, 'Hey, go add this Google Cloud functionality.' That is something that actually it feels like Google Cloud is really benefiting from. It is so broad and there is so much functionality there. We have a little bit of this problem with Stripe, where as we add more functionality to it, just the right way to navigate this big product surface area is an AI that's read all the API docs for you. That's working really well. The promise of AI being this orchestration layer for anything you think about, to my earlier question, even internally within the enterprise as a CEO, it's not like you don't have all the data, but how do you get it in one place, and you see it in the past that would have meant one more big ERP-ish project to go connect all the data sources, et cetera. Again, AI being this orchestration layer in a way that makes sense for the end user, I think it's been delightful to see. The bigger the product surface area, the more that benefit hits you. Again, we've seen that to some extent with Stripe, but I feel like with GCP, it must be just a massive effect."

**🇨🇳 精译**：说到谷歌云，我有一个产品请求，我一直在这个部分保留着，我知道你很期待。你本可以在X上发布它。没错。但是不，我要说一件非常好用的事情是GCP/MCP太棒了，你的AI可以通过编程方式与谷歌云交互。我猜你们几乎公开了所有东西，除了核心权限部分。我觉得在某种程度上，谷歌云的部分诅咒是功能太多了，我相信你偶尔会听到人们说。登录后有点难导航，你必须创建一个组织、一个项目等等，找到正确的服务，等等。现在，这一切都不重要了。你只要说，"嘿，去添加这个谷歌云功能。"这实际上是谷歌云真正受益的地方。它是如此广泛，有如此多的功能。我们在Stripe也有一点这个问题，随着我们添加更多功能，浏览这个庞大产品界面的正确方式是一个读过所有API文档的AI。这非常好用。AI作为你能想到的任何东西的编排层的前景，回到我之前的问题，即使在企业内部作为CEO，也不是你没有所有数据，而是你如何把它放在一个地方，你看到过去这意味着需要再做一个大型ERP类项目来连接所有数据源，等等。同样，AI以对最终用户有意义的方式成为这个编排层，我很高兴看到这一点。产品界面越大，这种好处就越明显。同样，我们在Stripe也在一定程度上看到了这一点，但我觉得对于GCP来说，这一定是一个巨大的效应。

---

**[Sundar Pichai]**：
> "I think we could do a lot better. But you're right, it's an immense opportunity, I think. I've been really happy with it. Then that gets to my product. Did you bring product suggestions for a second? You go first. I wanted to but— What's interesting me about OpenClaw and the product market fit of things like that, is they're allowing stateful AI for consumers. If you want to say the classic, 'Round up the daily news that I'm interested in and send it to me each morning,' or just something that involves persistence that none of the popular AI or mainstream AI apps allow persistence. Is that coming?"

**🇨🇳 精译**：我认为我们可以做得更好。但你说得对，这是一个巨大的机会，我认为。我对此非常满意。然后这就谈到了我的产品。你带产品建议来了吗？你先说。我想但——我对OpenClaw和类似产品的市场契合度感兴趣的是，它们为消费者提供了有状态的AI。如果你想说经典的，"汇总我感兴趣的每日新闻，每天早上发给我，"或者只是涉及持久性的东西，而流行的AI或主流AI应用都不允许持久性。这会实现吗？

---

**[Sundar Pichai]**：
> "I think directionally, look, I think you want to give users capability where you have persistent long-running tasks in a reliable, secure way. You have to think through things like identity, access, et cetera. But I think that's the future. That's the agentic future. Bringing that for consumers is a bit of an exciting frontier we are looking at. This is one of mine, too. This is Dreamer, which was the former CTO of Stripe's company that just got bought by Meta, I think, did a very good version of this. It was a very early view of... They were making custom software, including persistence, but also you could spec out— You can make your own little app. Exactly. They made that very easy to use. I feel like when people have this experience, there's a surprise and delight moment. It's just interesting to me that... Look, I think effectively the consumer interfaces are going to have full coding models underneath, and the right harnesses and the right skills and the ability to persist and run somewhere securely in the cloud, locally and in the cloud. All those primitives are coming together. What developers are… Today, I feel like there's 1% of the world, maybe not 1%, 0.1% of the world who's living this future. They are building stuff for themselves, but bringing that to mass adoption— Yes. Is a very exciting frontier, I think."

**🇨🇳 精译**：我认为方向上，看，我认为你想给用户提供能力，让他们能够以可靠、安全的方式拥有持久的长期运行任务。你必须考虑身份、访问等问题。但我认为这就是未来。这就是代理的未来。为消费者带来这一点是我们正在关注的一个令人兴奋的前沿领域。这也是我的一个想法。Dreamer是Stripe前CTO的公司，我想刚刚被Meta收购了，他们做了一个非常好的版本。这是一个非常早期的视角…他们在制作定制软件，包括持久性，但你也可以指定——你可以制作自己的小应用。没错。他们让这变得非常容易使用。我觉得当人们有这种体验时，会有惊喜和愉悦的时刻。我觉得有趣的是…看，我认为实际上消费者界面下面会有完整的编码模型，以及正确的工具和正确的技能，以及能够持久并安全地在云端、本地和云端运行的能力。所有这些基础要素正在汇聚。开发者现在…今天，我觉得世界上有1%的人，也许不是1%，而是0.1%的人正在体验这种未来。他们为自己构建东西，但将其推向大众采用——是的。我认为这是一个非常令人兴奋的前沿领域。

---

**[采访者]**：
> "My other product idea is, for some reason—I don't know if this is your lived experience, but certainly my lived experience—that search in Google Docs is so much harder than, say, search in Gmail. Obviously, they're both equally good search engines. But I think what's going on is keyword search works reasonably well for email because you can probably remember a unique set of keywords for that email. Whereas what always happens, at least to me, is I want to go back and look at the 2026 budget. It turns out if I search Google Slides for 2026 budget, neither of those words is particularly unique in the context of words that exist in PowerPoints at Stripe, and so I can never find the exact right one. I'm curious, does Sundar Pichai also have this problem?"

**🇨🇳 精译**：我的另一个产品想法是，出于某种原因——我不知道这是不是你的生活体验，但肯定是我的生活体验——谷歌文档中的搜索比Gmail中的搜索难得多。显然，它们都是同样优秀的搜索引擎。但我认为问题在于，关键词搜索对电子邮件相当有效，因为你可能记得那封邮件的一组独特关键词。而至少对我来说，总是发生的情况是，我想回去看2026年的预算。结果是，如果我在谷歌幻灯片中搜索2026年预算，这两个词在Stripe的PPT中都不是特别独特，所以我永远找不到正确的那个。我很好奇，Sundar Pichai也有这个问题吗？

---

**[Sundar Pichai]**：
> "Somehow, I haven't felt it as acutely as you're describing it, but when you describe it, it resonates well with my experience. I'm literally playing through the person to whom I'm going to play this segment of the conversation. I know exactly who I'm going to go talk to, the people who are working on it. I think we can make it a lot better. I think the AI integration into these services, including Google Docs, I think you will see sharp improvements in the coming months ahead. I think we all did the first versions of it where you just put it in somewhere. I think over time, what all can you keep in context, what can you cache and what can you really bring to bear. I think we can make a lot of progress on. I think we can do a lot better."

**🇨🇳 精译**：不知何故，我没有像你描述的那样强烈地感受到这个问题，但当你描述它时，它与我的体验很共鸣。我简直在脑补我要把这段对话放给谁看。我确切地知道我要去和谁谈，那些正在做这个的人。我认为我们可以做得更好。我认为AI集成到这些服务中，包括谷歌文档，我认为你会在未来几个月看到大幅改进。我认为我们都做了第一个版本，只是把它放在某个地方。我认为随着时间的推移，你可以保留多少上下文，你可以缓存什么，你真正可以应用什么。我认为我们可以取得很大进展。我认为我们可以做得更好。

---

**[采访者]**：
> "Great. We have a good— A lot of companies that I'm involved with, even ones that were started reasonably recently, have had to dramatically shift their workflows relative to product development, engineering practices. Who they even think of it should be on the design team and the capabilities of that. Are you revisiting all that at Google? Are you rethinking it? Has there been big shifts in workflow or other aspects?"

**🇨🇳 精译**：太好了。我们有一个很好的——我参与的很多公司，即使是最近成立的公司，都不得不相对于产品开发、工程实践大幅改变他们的工作流程。他们甚至认为谁应该在设计团队以及设计团队的能力。谷歌在重新审视这一切吗？你在重新思考吗？工作流程或其他方面有大的转变吗？

---

**[Sundar Pichai]**：
> "The way I would say it is, you can think of it as concentric circles. There are some groups within Google who are shifting more profoundly. For me, a big task is how do you diffuse that to more and more groups, particularly in 2026? Some of it, we couldn't do it early because it breaks so often that, it's almost like you see this promising new world, but it's semi-broken. But this year, I feel like the curve is shifting pretty dramatically. I can see groups, and particularly, I would say GDM and some of the SWE groups really change their workflows. They are using, we call this for some strange reason, we have a different name internally than externally of the same product, but it's Jet Ski internally, which is Antigravity. You're living on it, you're living in an agent manager world, you have workflows, and you're working in this new way. But just last week, we rolled it out to the Search team. We're constantly pushing that. In a large organization, I think change management is a hard aspect of this technology diffusing, which may be easy for a small company. You can quickly switch over."

**🇨🇳 精译**：我会这样说，你可以把它看作是同心圆。谷歌内部有一些团队正在经历更深刻的转变。对我来说，一个重要的任务是如何将这种转变扩散到越来越多的团队，特别是在2026年？有些事情我们早期做不到，因为它经常出问题，几乎就像你看到了这个充满希望的新世界，但它还半崩溃着。但今年，我感觉曲线正在发生相当大的变化。我可以看到一些团队，特别是GDM和一些软件工程团队真的改变了他们的工作流程。他们在使用，出于某种奇怪的原因，我们内部对同一个产品有不同的名称，内部叫Jet Ski，也就是Antigravity。你生活在其中，生活在一个代理管理器的世界里，你有工作流程，你以这种新的方式工作。但就在上周，我们把它推广到了搜索团队。我们一直在推动这一点。在一个大型组织中，我认为变革管理是这项技术扩散的一个难点，这对于小公司来说可能很容易。你可以很快切换过去。

---

**[采访者]**：
> "Can I add a few problems I see when it comes to actual diffusion of AI in industry? I'm curious how and when you think we'll solve them. Because as I see it, we have a big intelligence overhang. The AIs are now amazing in terms of what they can do in the abstract. If you look at how AI-native a company is or just how much it uses that intelligence, there'll probably be a shortfall. The problems that I see are something like, one: it actually takes a while to get good as an engineer at prompting your AI well. You can prompt AI better or worse to write code. Then there's a lot of, say, Stripe-specific prompting in our case to know which tools to use. There's the general being good at prompting, and then there's the Stripe being good at prompting. Then, of course, you have the fact that it's hard to share an AI-generated code base because you have a blast radius, and you're just changing so much and the turnover of the code is high enough where maybe you're rewriting it several times before you ship, that it's hard for many people to collaborate on the code base versus before when the code velocity was slower. Then as you go outside of engineering, the big one I see is access to data where you'd like to have your agent go, 'How many times a day do people at companies around the world say, "Hey, what's the status of this deal?"' That is like information that the company knows and should be agentically answerable. We actually have some cool stuff at Stripe where I was seeing where you can actually answer that pretty well. But with both habits and access to data, and as you get into a bigger company, the permissions engine of who can actually get access to this data, that all needs to be rewritten. Then you get into role definition where, like you were saying, Eng, PM, design stems a little bit from a prior year. You may want to, at least in some cases, merge those roles a little bit as AI gets better at all those since you've got a product... Anyway, that's my characterization of—in 2026—the models are capable of this, but we're only using them so much. What do you think that adoption of the intelligence looks like?"

**🇨🇳 精译**：我可以补充几个我看到的关于AI在行业中实际扩散的问题吗？我很好奇你认为我们会如何以及何时解决这些问题。因为在我看来，我们有一个巨大的智能悬顶。AI现在在抽象能力方面非常惊人。如果你看看一家公司的AI原生程度，或者它使用这种智能的程度，可能会有差距。我看到的问题比如：第一，作为一名工程师，要擅长用好的提示词调用AI实际上需要一段时间。你写的提示词好坏会影响AI写代码的质量。比如在我们Stripe，有很多特定于Stripe的提示词，要知道使用哪些工具。有通用的提示词技巧，也有Stripe特定的提示词技巧。然后，当然还有一个事实是，共享AI生成的代码库很难，因为影响范围很大，你修改的东西太多，代码的周转率足够高，你可能在发布前重写好几次，与之前代码速度较慢的时候相比，很多人很难在代码库上协作。当你走出工程领域，我看到的最大问题是数据访问，你想让你的代理去查询，"世界各地公司的人们每天会说多少次，'嘿，这笔交易的状态如何？'"这是公司知道的信息，应该可以通过代理回答。我们在Stripe实际上有一些很酷的功能，我看到你可以很好地回答这个问题。但既有习惯问题，也有数据访问问题，而且当你进入更大的公司时，谁实际上可以访问这些数据的权限引擎，这些都需要重写。然后你进入角色定义，就像你说的，工程师、产品经理、设计源于前一个时代。你可能希望，至少在某些情况下，随着AI在所有这些方面变得更好，合并这些角色，因为你有一个产品…无论如何，这是我对2026年的描述——模型有能力做到这一点，但我们对它们的使用还很有限。你认为这种智能的采用会是什么样子？

---

**[Sundar Pichai]**：
> "Look, a lot of us are working on literally what the Gemini team... The Gemini enterprise teams and the Antigravity teams, they're all precisely working on these problems. This is the roadmap you're talking about, right? That's literally we are using it internally, running into these barriers, working past it. That's the products that are shipping. We are still diffusing it because what you do is people, as part of using it, like if you're the SRE team at Google, you suddenly find portions which you can create an automated workflow. That's happening in these spots. But doing it more systematically when you develop skills, how does it get centralized? How is it available to the models and for everyone to use? Identity access controls are real hard problems, and so we are working through those things. But those are the key things which are limiting diffusion to us, too. We take security a lot more seriously, and so we have to. That is another layer on top of all these things, the cost of mistakes when you're running these services, we have to work through it. But I think because of it, when we solve it, I think we will bring it in a more robust way, which will help. I feel like we're going through that fixed cost right now, but you will see this jump of what people are able to do when we bring it outside, and others are doing it, too. In a more robust way, the models are improving."

**🇨🇳 精译**：我们很多人确实在做这些工作，Gemini团队…Gemini企业团队和Antigravity团队，他们都正是在解决这些问题。这就是你所说的路线图，对吧？我们确实在内部使用它，遇到这些障碍，克服它们。这就是正在发布的产品。我们仍在推广它，因为人们在使用它的过程中，比如如果你是谷歌的站点可靠性工程团队，你突然发现有些部分可以创建自动化工作流。这些点正在发生。但当你开发技能时，要更系统地做这件事，它如何被集中管理？模型如何使用它，所有人如何使用它？身份访问控制是非常难的问题，所以我们正在解决这些问题。但这些也是限制我们内部推广的关键因素。我们对安全更加重视，所以我们必须这样做。这是所有这些事情之上的另一层，运行这些服务时出错的代价，我们必须解决这个问题。但我认为正因为如此，当我们解决它时，我们会以更稳健的方式推出它，这会有所帮助。我觉得我们现在正在经历这个固定成本阶段，但当我们把它推向外部时，你会看到人们能够做的事情会有一个跳跃，其他人也在这样做。模型正在以更稳健的方式改进。

---

**[采访者]**：
> "Google re-forecasts its business a few times a year, formally, I presume. At least we do at Stripe where we set a budget for the year, and then three times a year we produce a formal re-forecast. When you think about it, a re-forecast is a moment in time function where you take the state of the business, some of which is in people's heads, but most of which is written down everywhere where it's like, 'How is this product doing? How is that product doing? Will this deal close? Will that happen?' Whatever. There's the moment in time state of the business, we put it into a function and out comes the updated numbers for the year. You can imagine an AI doing a fully, no human in the loop, forecast? What quarter do you think Google's first fully agentic forecast is?"

**🇨🇳 精译**：谷歌每年会正式重新预测几次业务，我猜是这样。至少我们Stripe是这样做的，我们制定年度预算，然后每年三次发布正式的重新预测。当你思考这个问题时，重新预测是一个时间点函数，你获取业务状态，其中一些在人们的脑子里，但大部分都写在各个地方，比如"这个产品表现如何？那个产品表现如何？这笔交易能完成吗？那事会发生吗？"不管是什么。有了业务的时间点状态，我们把它放到一个函数里，就得出了当年的更新数字。你能想象AI做一个完全不需要人类参与的预测吗？你认为谷歌第一次完全由代理做的预测会在哪个季度？

---

**[Sundar Pichai]**：
> "I definitely expect in some of these areas, '27, to be an important inflection point for certain things. Even the people doing it, that is the workflow through which they would produce it. Maybe for a while, you would check it in the conventional way, but you switch over, a crossover. But I expect '27 to be a big year in which some of those shifts happen pretty profoundly. I think that was Elad's question was, Eng is an early adopter, but outside of Eng… Okay, it sounds like you think '27, a lot of these non-Eng processes really start— I do think your question earlier on, I think you were asking in the context of Waymo or robotics companies. I do think companies which are… That's one advantage startups are going to have. More AI-native teams, and you can probably get at it through your interview processes, et cetera. Whereas for us, we would have retraining, transformation, et cetera. I think that's maybe an advantage the younger companies are going to have. We have to drive that transformation."

**🇨🇳 精译**：我肯定预计在其中一些领域，2027年将成为某些事情的重要转折点。即使是现在做这些工作的人，那也是他们生成预测的工作流程。也许有一段时间，你会用传统方式检查它，但你会切换过去，一个交叉点。但我预计2027年将是重要的一年，其中一些转变会非常深刻地发生。我想那是Elad的问题，工程是早期采用者，但在工程之外…好的，听起来你认为2027年，很多这些非工程流程真正开始——我确实认为你之前的问题，我想你是在Waymo或机器人公司的背景下问的。我确实认为那些…这是创业公司将拥有的一个优势。更多AI原生团队，你可能可以通过面试流程等实现这一点。而对我们来说，我们需要再培训、转型等等。我认为这可能是年轻公司将拥有的一个优势。我们必须推动这种转型。

---

**[采访者]**：
> "Last question. We're talking a lot about initiatives that started small at Google, like the Transformer, which is not Google's main priority when that initiative started. What's a small thing inside Google that you're excited about these days?"

**🇨🇳 精译**：最后一个问题。我们谈了很多谷歌从小开始的项目，比如Transformer，在这个项目开始时它并不是谷歌的主要优先级。现在谷歌内部有什么小事情让你感到兴奋？

---

**[Sundar Pichai]**：
> "It probably would surprise people. When we decided to do data centers in space, we started as a very small team. It's literally a few people with a small budget to go to the first milestone. I think it's important to start small, even if it's a big idea. That is an example of a small thing. Look, I literally spent time yesterday who was explaining some improvement in post-training, which is one person talking through the improvement they are doing, listening to it, I'm like, 'Oh, it's going to really show up as a nice jump.' That's the constant power of this moment. All of that, I don't want to be specific about the second one, but we'll publish it one day, I'm sure. But those are some of the small jumps I'm excited about. There's data centers in space and new ML techniques. Yeah."

**🇨🇳 精译**：这可能会让人们感到惊讶。当我们决定做太空数据中心时，我们从一个非常小的团队开始。实际上只有几个人，用很小的预算去实现第一个里程碑。我认为从小处开始很重要，即使是一个大想法。这是小项目的一个例子。我昨天还花时间听一个人解释后训练方面的一些改进，他们在讲解自己正在做的改进，听着听着我就想，"哦，这会带来一个很好的性能跃升。"这就是这个时刻的持续力量。所有这些，我不想具体说明第二个是什么，但我肯定有一天我们会公布它。但这些是我感到兴奋的一些小跃升。有太空数据中心和新的机器学习技术。是的。

---

**[采访者]**：
> "Great answer. Sundar, thank you. All right. Real pleasure. Thanks. Take care."

**🇨🇳 精译**：好答案。Sundar，谢谢你。好的。非常荣幸。谢谢。保重。

---

### 4. NotebookLM深度研究追问
1. **谷歌的TPU分配机制**：谷歌内部不同部门（搜索、YouTube、Waymo等）的TPU资源分配是否有明确的优先级规则？Pichai提到每周花一小时进行"细粒度"计算单元分配，这一决策过程的具体框架是什么？
2. **LaMDA与ChatGPT的竞品时间线**：根据Pichai的说法，谷歌在2022年Google I/O上展示的AI Test Kitchen实际上就是LaMDA，但内部版本"毒性太高"无法发布。同时，OpenAI的ChatGPT在2022年11月低调发布。这两者的具体技术参数、安全性评估标准和商业化准备度对比分析是什么？
3. **供应链约束的量化影响**：Pichai提到内存是AI行业"最关键组件"，且2026-2027年的内存供应可能成为行业瓶颈。这一约束的具体量化影响是什么？按谷歌1750-1850亿美元CapEx计划，内存成本占比多少？这一瓶颈将如何影响AI模型的规模和部署速度？
4. **谷歌的AGI战略与风险容忍度**：Pichai表示谷歌的创始人"可能都AGI-pilled"，但作为一个大公司，对产品质量有更高标准。这种文化差异如何影响谷歌在AI竞赛中的风险承受能力和创新速度？与OpenAI等更灵活的竞争对手相比，这种"更高质量门槛"是优势还是劣势？
5. **太空数据中心的可行性研究**：Pichai提到谷歌正在"最早阶段"思考太空数据中心，并类比2010年的Waymo项目。这一概念的实际技术可行性、成本结构、部署时间表和商业应用场景的具体研究和预测是什么？
6. **AI企业落地的组织变革**：Pichai提到2027年将是AI在企业非工程流程中应用的关键转折点。谷歌内部推动AI工作流扩散面临的最大组织障碍是什么？大公司与初创公司在AI转型中的核心优劣势差异是什么？
7. **端到端自动驾驶的技术跃迁**：Waymo最近的突破来自于端到端深度学习的应用，而不是之前基于规则的系统。这种技术范式的转变如何影响自动驾驶的落地时间表和成本结构？谷歌在这方面的技术积累如何转化为市场竞争优势？