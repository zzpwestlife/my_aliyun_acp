# 阿里云大模型 ACP 术语表 Glossary

> 依据 [阿里云大模型ACP考试大纲-V3.pdf](file:///Users/joeyzou/Code/OpenSource/my_aliyun_acp/exam_materials/common/%E9%98%BF%E9%87%8C%E4%BA%91%E5%A4%A7%E6%A8%A1%E5%9E%8BACP%E8%80%83%E8%AF%95%E5%A4%A7%E7%BA%B2-V3.pdf) 整理，并结合本仓库已有 ACP 学习笔记补充高频英文名词、参数名和缩写。
> 用法建议：这里主要用于查词；参数对比、RAGAS 四指标、训练/微调/量化/部署辨析请看 [ACP易混淆概念辨析.md](file:///Users/joeyzou/Code/OpenSource/my_aliyun_acp/exam_materials/common/ACP%E6%98%93%E6%B7%B7%E6%B7%86%E6%A6%82%E5%BF%B5%E8%BE%A8%E6%9E%90.md)。

## Glossary A-Z

### A

#### ACP

- 全称：`Alibaba Cloud Certified Professional`
- 在本考试里特指：阿里云大模型高级工程师 ACP 认证。
- 一句话记忆：ACP 是认证级别，不是某个模型或平台名称。

#### Agent

- 中文：智能体。
- 含义：不仅能回答问题，还能调用工具、规划步骤、执行任务。
- 易混点：会回答问题不等于会办事；问答更偏大模型 + RAG，执行任务更偏 Agent。

#### API

- 全称：`Application Programming Interface`
- 中文：应用程序编程接口。
- 在考试里常指：通过 API 调用大模型、Assistant、云服务能力。

#### Assistant API

- 中文：百炼 Assistant API。
- 作用：用于构建智能体、多轮对话、多模态助手等。
- 易混点：它不是单纯模型参数接口，而是更贴近“应用层智能体”的能力接口。

#### Auto-Merging / AutoMerging

- 中文：自动合并检索。
- 作用：多个子块同时命中时，向上合并召回它们的父块。
- 易混点：它不是简单增大 chunk，而是基于层级结构的召回策略。

### B

#### base\_url

- 中文：接口基地址。
- 在百炼 OpenAI 兼容调用里，高频考点是：

```text
https://dashscope.aliyuncs.com/compatible-mode/v1
```

- 易混点：容易误填成 `openai.com`、百炼控制台地址，或漏掉 `/compatible-mode/v1`。

#### Batch Generation

- 中文：批量/非流式生成。
- 含义：完整生成后一次返回结果。
- 对比：与 `stream=True` 相对，更适合后台任务或一次性取完整结果。

#### Blackboard

- 中文：黑板式协作。
- 含义：多个 Agent 围绕共享中间状态并行读写、迭代协作。
- 易混点：它不是固定工作流，也不是 Leader-Worker。

### C

#### Chunk

- 中文：文本切片后的片段。
- 在 RAG 中，文档常先被切成多个 chunk 再向量化入库。
- 易混点：chunk 太大容易混入噪声，太小又可能丢上下文。

#### Context Engineering

- 中文：上下文工程。
- 含义：不是只写提示词，而是统筹 `Prompt`、`RAG`、`Tool`、`Memory` 等，把最合适的上下文动态送给模型。
- 易混点：不要把它缩窄成“只优化模板”。

#### context\_precision

- 中文：上下文精确率。
- 在 `RAGAS` 中表示召回的上下文里有多少是相关的。
- 低意味着：噪声多、召回结果不够准。
- 详细辨析：见 [ACP易混淆概念辨析.md](file:///Users/joeyzou/Code/OpenSource/my_aliyun_acp/exam_materials/common/ACP%E6%98%93%E6%B7%B7%E6%B7%86%E6%A6%82%E5%BF%B5%E8%BE%A8%E6%9E%90.md) 的 `RAGAS 四指标辨析`。

#### context\_recall

- 中文：上下文召回率。
- 在 `RAGAS` 中表示回答问题所需信息是否被充分召回。
- 低意味着：没找全、缺少关键信息。
- 详细辨析：见 [ACP易混淆概念辨析.md](file:///Users/joeyzou/Code/OpenSource/my_aliyun_acp/exam_materials/common/ACP%E6%98%93%E6%B7%B7%E6%B7%86%E6%A6%82%E5%BF%B5%E8%BE%A8%E6%9E%90.md) 的 `RAGAS 四指标辨析`。

#### CoT

- 全称：`Chain of Thought`
- 中文：思维链。
- 作用：引导模型分步推理，提升复杂任务正确率。
- 易混点：它更适合复杂推理，不是所有简单任务都值得用。

### D

#### Deployment

- 中文：部署。
- 含义：把模型真正放到可运行环境中，对外提供服务，例如部署到 `ECS`、`PAI-EAS`、`FC`、百炼或 `vLLM` 推理服务中。
- 关注点：能不能跑起来、响应快不快、并发高不高、成本是否可控、服务是否稳定。
- 易混点：部署不是训练，也不是让模型学新知识；它解决的是“怎么上线使用”。
- 详细辨析：见 [ACP易混淆概念辨析.md](file:///Users/joeyzou/Code/OpenSource/my_aliyun_acp/exam_materials/common/ACP%E6%98%93%E6%B7%B7%E6%B7%86%E6%A6%82%E5%BF%B5%E8%BE%A8%E6%9E%90.md) 的 `训练、微调、量化、部署辨析`。

### E

#### ECS

- 全称：`Elastic Compute Service`
- 中文：云服务器 ECS。
- 在考试里常和 `FC`、`PAI-EAS` 一起考部署选型。

#### Embedding

- 中文：嵌入向量，或向量化表示。
- 含义：把文本映射成一串数字向量，让机器能比较语义相似度。
- 一句话记忆：`Embedding` 是把文本放到“语义地图”上。

### F

#### Fine-tuning

- 中文：微调。
- 含义：在已经训练好的基础模型上，再用特定任务数据继续训练，让模型更适合某个场景。
- 适合场景：固定风格、固定格式、领域行为稳定化、特定任务表现增强。
- 不适合优先解决的问题：最新知识、私有知识、频繁变化知识，这类通常先考虑 `RAG`。
- 易混点：微调是训练的一种，不等于从零训练；它主要改变“模型怎么表现”，不是补“最新事实知识”。
- 详细辨析：见 [ACP易混淆概念辨析.md](file:///Users/joeyzou/Code/OpenSource/my_aliyun_acp/exam_materials/common/ACP%E6%98%93%E6%B7%B7%E6%B7%86%E6%A6%82%E5%BF%B5%E8%BE%A8%E6%9E%90.md) 的 `训练、微调、量化、部署辨析`。

#### faithfulness

- 中文：忠实度。
- 在 `RAGAS` 中衡量答案是否忠于检索上下文。
- 低意味着：答案里出现了上下文未支持的内容，也就是幻觉。
- 详细辨析：见 [ACP易混淆概念辨析.md](file:///Users/joeyzou/Code/OpenSource/my_aliyun_acp/exam_materials/common/ACP%E6%98%93%E6%B7%B7%E6%B7%86%E6%A6%82%E5%BF%B5%E8%BE%A8%E6%9E%90.md) 的 `RAGAS 四指标辨析`。

#### FC

- 全称：函数计算 `Function Compute`
- 特点：Serverless、按量付费、适合低频突发和快速发布。
- 易混点：不适合持续高并发的大模型常驻推理。

#### Few-shot

- 中文：少样本提示。
- 含义：在提示词中给几个输入-输出示例，帮助模型更稳定完成任务。
- 易混点：Few-shot 是提示词技术，不是微调。

### G

#### GoT

- 全称：`Graph of Thoughts`
- 中文：思维图。
- 含义：可视为 `CoT` 的扩展形式之一。

### J

#### JSONL

- 全称：`JSON Lines`
- 中文：一行一个 JSON 对象的数据格式。
- 在微调里常用于组织 `instruction/input/output` 样本。

### L

#### LangChain

- 中文：大模型应用开发框架。
- 在考纲中与 `LlamaIndex`、`Dify` 一起出现，属于常见开发组件。

#### LlamaIndex

- 中文：以 RAG 为核心的大模型应用开发框架。
- 在考试里高频出现于：构建 RAG、召回优化、句子窗口、自动合并等。

#### LoRA

- 全称：`Low-Rank Adaptation`
- 中文：低秩适配。
- 作用：只训练少量新增参数，实现参数高效微调。
- 易混点：LoRA 是微调方法，不是量化方法。

### M

#### Memory

- 中文：记忆机制。
- 在 Agent 场景里通常分为短期记忆（上下文）和长期记忆（外部存储 + 检索）。
- 易混点：大模型 API 默认无状态，不自带真正的跨会话长期记忆。

#### Meta Prompting

- 中文：元提示。
- 含义：让模型帮助设计、改写、优化提示词本身。
- 易混点：它不是多图拼接，也不是上下文工程的同义词。

#### Multi-agent

- 中文：多智能体。
- 含义：多个 Agent 分工协作完成更复杂的任务。

### O

#### OpenAI-Compatible API

- 中文：OpenAI 兼容接口。
- 含义：用接近 OpenAI SDK/消息结构的方式调用百炼模型。
- 高频点：`base_url`、`messages`、`stream=True`、`temperature`、`top_p`。

### P

#### PagedAttention

- 中文：分页注意力。
- 是 `vLLM` 的核心能力之一，用于提升高并发推理吞吐。
- 一句话记忆：它属于推理优化，不属于训练算法。

#### PAI / PAI-EAS

- `PAI`：阿里云机器学习平台。
- `PAI-EAS`：更偏在线推理服务部署。
- 考试里常与 `ECS`、`FC` 一起考“部署载体选型”。

#### Plan & Execute

- 中文：规划后执行。
- 含义：先由模型规划步骤，再逐步执行。
- 易混点：固定流程、可审计要求强时，不一定比固定工作流更合适。

#### Prompt

- 中文：提示词。
- 含义：给模型的任务说明、上下文、约束和输出格式要求。
- 易混点：Prompt 是“怎么问”，不是“补知识”的主要手段。

### Q

#### Quantization

- 中文：量化。
- 含义：把模型参数从更高精度压缩为更低精度表示，以降低显存占用、推理成本和部署门槛。
- 常见用途：推理优化、部署前压缩、降低线上资源成本。
- 易混点：量化不是训练，不是在教模型新能力；它主要解决“模型能不能更省资源地跑起来”。
- 详细辨析：见 [ACP易混淆概念辨析.md](file:///Users/joeyzou/Code/OpenSource/my_aliyun_acp/exam_materials/common/ACP%E6%98%93%E6%B7%B7%E6%B7%86%E6%A6%82%E5%BF%B5%E8%BE%A8%E6%9E%90.md) 的 `训练、微调、量化、部署辨析`。

#### Qwen Code

- 中文：通义千问代码 Agent / CLI 编码智能体实践。
- 在考试里更偏 Agent 工具实践，不是单纯模型名称考点。

### R

#### RAG

- 全称：`Retrieval-Augmented Generation`
- 中文：检索增强生成。
- 作用：先检索外部知识，再结合检索结果生成回答。
- 易混点：RAG 主要补知识和时效，不是提升模型纯推理能力。

#### RAGAS

- 中文：RAG 自动化评测指标体系。
- 高频指标：
  - `faithfulness`
  - `answer_relevancy`
  - `context_precision`
  - `context_recall`
- 详细辨析：见 [ACP易混淆概念辨析.md](file:///Users/joeyzou/Code/OpenSource/my_aliyun_acp/exam_materials/common/ACP%E6%98%93%E6%B7%B7%E6%B7%86%E6%A6%82%E5%BF%B5%E8%BE%A8%E6%9E%90.md) 的 `RAGAS 四指标辨析`。

#### ReAct

- 全称：`Reason + Act`
- 中文：推理与行动交替。
- 常见于 Agent 工作流设计。

#### Rerank / Reranking

- 中文：重排序。
- 作用：对初步召回的结果再做一次精排，把更相关的内容排前面。
- 易混点：它和召回不是同一步，但常一起被归到“检索链路优化”。

### S

#### Sentence Window

- 中文：句子窗口检索。
- 含义：以句子为命中单元，命中后返回前后扩展窗口作为上下文。
- 易混点：它和 Auto-Merging 是两种不同的召回优化思路。

#### Skill

- 中文：技能模块。
- 在 Agent 系统里，表示把流程固化成可复用、可共享、可演进的能力。

#### stream

- 常见写法：`stream=True`
- 中文：流式返回。
- 含义：模型一边生成，一边把结果持续返回给前端或调用方。

#### system / user / assistant

- 中文：消息角色。
- 用途：
  - `system`：设定身份、风格、行为边界
  - `user`：用户输入
  - `assistant`：模型历史输出
- 高频点：多轮对话时要把历史消息按角色显式传入 `messages`。

### T

#### temperature

- 中文：采样温度。
- 作用：控制输出随机性强弱。
- 详细辨析：见 [ACP易混淆概念辨析.md](file:///Users/joeyzou/Code/OpenSource/my_aliyun_acp/exam_materials/common/ACP%E6%98%93%E6%B7%B7%E6%B7%86%E6%A6%82%E5%BF%B5%E8%BE%A8%E6%9E%90.md) 的 `Temperature、Top-P、Top-K 辨析`。

#### Token

- 中文：模型处理文本时的基本切分单位。
- 备注：模型通常是按 token 一步步生成，不是按整句一次性生成。

#### Training

- 中文：训练。
- 含义：用数据更新模型参数，让模型学会某种能力。
- 范围：训练是大概念，既包括预训练，也包括微调。
- 易混点：很多人把训练和微调当成同义词，其实微调只是训练中的一种更小范围做法。
- 详细辨析：见 [ACP易混淆概念辨析.md](file:///Users/joeyzou/Code/OpenSource/my_aliyun_acp/exam_materials/common/ACP%E6%98%93%E6%B7%B7%E6%B7%86%E6%A6%82%E5%BF%B5%E8%BE%A8%E6%9E%90.md) 的 `训练、微调、量化、部署辨析`。

#### ToT

- 全称：`Tree of Thoughts`
- 中文：思维树。
- 含义：`CoT` 的扩展方法之一。

#### Top-K

- 中文：按前 `K` 个高概率 token 采样。
- 作用：控制候选数量上限。
- 详细辨析：见 [ACP易混淆概念辨析.md](file:///Users/joeyzou/Code/OpenSource/my_aliyun_acp/exam_materials/common/ACP%E6%98%93%E6%B7%B7%E6%B7%86%E6%A6%82%E5%BF%B5%E8%BE%A8%E6%9E%90.md) 的 `Temperature、Top-P、Top-K 辨析`。

#### top\_p

- 中文：核采样参数。
- 作用：按累计概率截断候选集。
- 详细辨析：见 [ACP易混淆概念辨析.md](file:///Users/joeyzou/Code/OpenSource/my_aliyun_acp/exam_materials/common/ACP%E6%98%93%E6%B7%B7%E6%B7%86%E6%A6%82%E5%BF%B5%E8%BE%A8%E6%9E%90.md) 的 `Temperature、Top-P、Top-K 辨析`。

### V

#### vLLM

- 中文：高吞吐大模型推理部署框架。
- 关键词：`PagedAttention`、高并发、推理服务。
- 易混点：它不是微调训练框架。

### Z

#### Zero-shot

- 中文：零样本提示。
- 含义：不给示例，直接让模型完成任务。
- 对比：和 `Few-shot` 的差别在于是否给示例。

## 高频缩写小抄

| 缩写/术语      | 中文        | 考试最该记住的一句话     |
| ---------- | --------- | -------------- |
| `ACP`      | 阿里云高级认证   | 这是认证级别，不是模型名   |
| `API`      | 接口        | 常考大模型调用方式与参数   |
| `CoT`      | 思维链       | 复杂任务可引导分步推理    |
| `ECS`      | 云服务器      | 常驻部署常见载体       |
| `FC`       | 函数计算      | 低频突发、快速发布、按量付费 |
| `Few-shot` | 少样本提示     | 给示例，不是微调       |
| `GoT`      | 思维图       | `CoT` 的扩展      |
| `JSONL`    | 一行一个 JSON | 微调数据常见格式       |
| `LoRA`     | 低秩适配      | 参数高效微调，不是量化    |
| `Quantization` | 量化 | 压缩推理成本，不是训练 |
| `RAG`      | 检索增强生成    | 补知识、补时效，不是补推理力 |
| `RAGAS`    | RAG 评测体系  | 重点看四个指标辨析      |
| `Training` | 训练 | 大概念，微调属于训练 |
| `ToT`      | 思维树       | `CoT` 的扩展      |
| `vLLM`     | 推理部署框架    | 推理，不是训练        |

## 最后速记

- `RAG`：解决知识范围与时效问题。
- `LoRA`：省参数地做微调。
- `vLLM`：做高吞吐推理部署。
- `FC`：适合低频突发与快速发布。
