# 阿里云大模型 ACP 考前最后 5 分钟速看版

> 这份文档只保留最容易考、最容易混的判断原则。
> 完整解释见 [ACP易混淆概念辨析.md](file:///Users/joeyzou/Code/OpenSource/my_aliyun_acp/exam_materials/common/ACP%E6%98%93%E6%B7%B7%E6%B7%86%E6%A6%82%E5%BF%B5%E8%BE%A8%E6%9E%90.md) 和 [ACP术语表_glossary.md](file:///Users/joeyzou/Code/OpenSource/my_aliyun_acp/exam_materials/common/ACP%E6%9C%AF%E8%AF%AD%E8%A1%A8_glossary.md)。

## 参数

- `Temperature`：控制随机性，不控制长度。
- `Top-P`：按累计概率截断候选集。
- `Top-K`：按候选数量截断候选集。
- `stream=True`：改善交互体验，不直接提升答案质量。

## RAG

- `RAG`：补知识、补时效，不是补推理力。
- `Embedding`：把文本放到语义空间里。
- `Rerank`：对召回结果二次精排。
- `Sentence Window`：命中一句，补前后上下文。
- `Auto-Merging`：多个子块命中，向上合并父块。

## RAGAS

- `context_precision`：找得准不准。
- `context_recall`：找得全不全。
- `faithfulness`：有没有胡编。
- `answer_relevancy`：有没有答对题。

## 选型

- `Prompt`：改提问方式。
- `RAG`：补外部知识。
- `Fine-tuning`：固化风格、格式、任务行为。
- 题目强调“最新知识、私有文档、知识常变化”：优先 `RAG`。
- 题目强调“固定 JSON、固定口吻、长期稳定输出”：优先 `Fine-tuning`。

## 训练

- `Training`：让模型学。
- `Fine-tuning`：训练的一种。
- `Distillation`：让小模型学大模型。
- `Quantization`：让模型更轻、更省资源，不是训练。
- `Deployment`：让模型上线跑起来。

## Agent

- `Function Calling`：结构化调工具。
- `ReAct`：思考-行动-观察循环。
- `MCP`：标准化接入和发现工具。
- `Prompt`：一次性会话指令。
- `Skill`：可复用、可版本化的流程能力。

## 协作

- 固定工作流：流程稳定、可审计。
- `Plan & Execute`：变化多、异常多、流程不稳定。
- `Leader-Worker`：有总控，适合清晰拆解任务。
- `handoff`：顺序交接控制权。
- `Blackboard`：共享空间共创，适合开放式任务。

## 记忆

- 短期记忆：保当前会话。
- 长期记忆：保跨会话关键信息。
- 截断：直接丢早期内容。
- 滚动摘要：压缩旧对话保重点。

## 部署

- 托管 API / 百炼：快速上线、免运维。
- `FC`：低频、突发、按量付费。
- `PAI-EAS`：稳定在线推理。
- `ECS`：高度自定义，但运维复杂。
- `vLLM`：推理框架，不是训练框架，也不是云服务。

## 五组口诀

- 缺知识：先想 `RAG`
- 缺稳定格式：先想 `Fine-tuning`
- 缺低成本推理：先想 `Quantization`
- 要结构化调工具：先想 `Function Calling`
- 要高并发在线推理：先想 `PAI-EAS / ECS + vLLM`
