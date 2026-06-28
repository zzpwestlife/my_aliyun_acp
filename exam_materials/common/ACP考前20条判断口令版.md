# 阿里云大模型 ACP 考前 20 条判断口令版

> 用法：临考前快速扫一遍，每条只记“正确口径”和“别混成什么”。
> 完整解释见 [ACP易混淆概念辨析.md](file:///Users/joeyzou/Code/OpenSource/my_aliyun_acp/exam_materials/common/ACP%E6%98%93%E6%B7%B7%E6%B7%86%E6%A6%82%E5%BF%B5%E8%BE%A8%E6%9E%90.md) 和 [ACP考前最后5分钟速看版.md](file:///Users/joeyzou/Code/OpenSource/my_aliyun_acp/exam_materials/common/ACP%E8%80%83%E5%89%8D%E6%9C%80%E5%90%8E5%E5%88%86%E9%92%9F%E9%80%9F%E7%9C%8B%E7%89%88.md)。

## 20 条口令

1. `Temperature` 控随机，不控长度。  
   别混成：`top_p`、`top_k`

2. `Top-P` 看累计概率，不看固定数量。  
   别混成：`Top-K`

3. `Top-K` 看候选个数，不看累计概率。  
   别混成：`Top-P`

4. `stream=True` 提升交互体验，不直接提升答案质量。  
   别混成：提升准确率的参数

5. `RAG` 解决知识范围和时效问题，不是提升纯推理力。  
   别混成：`CoT`、微调

6. `Embedding` 决定找不找得到，`Rerank` 决定排得准不准。  
   别混成：两个都当成同一步

7. `context_recall` 看找全，`context_precision` 看找准。  
   别混成：答案质量指标

8. `faithfulness` 看有没有胡编，`answer_relevancy` 看有没有答对题。  
   别混成：两个都当“切题”

9. 私有知识、知识常变化、知识量大，优先想 `RAG`。  
   别混成：先微调

10. 固定风格、固定格式、长期稳定输出，优先想 `Fine-tuning`。  
    别混成：`RAG`

11. `Prompt` 是改提问方式，不是补知识主手段。  
    别混成：`RAG`

12. `Fine-tuning` 是训练的一种，`Quantization` 不是训练。  
    别混成：把量化当训练

13. `Distillation` 是让小模型学大模型，`Quantization` 是让模型更轻。  
    别混成：蒸馏等于量化

14. `Deployment` 是让模型上线跑起来，不是让模型学新知识。  
    别混成：训练或微调

15. `Function Calling` 解决结构化调工具，`ReAct` 解决边想边调边观察。  
    别混成：两者完全等价

16. `MCP` 是标准化接工具，不等于一次 `Function Calling`。  
    别混成：把协议当单次调用

17. 稳定流程优先固定工作流，变化多再用 `Plan & Execute`。  
    别混成：越智能越好

18. `Leader-Worker` 有总控，`Blackboard` 围绕共享空间共创。  
    别混成：两者都是普通多 Agent

19. `Skill` 是可复用流程包，`Prompt` 是会话里的临时说明。  
    别混成：Skill 只是长 Prompt

20. `vLLM` 是推理框架，`FC` 适合低频突发，`PAI-EAS` 适合稳定在线推理。  
    别混成：`vLLM` 是训练框架，或 `FC` 适合持续高并发

## 最后连读版

- 参数先分清：`Temperature` 控随机，`Top-P` 看累计概率，`Top-K` 看候选数量。
- RAG 先分层：`Embedding` 找，`Rerank` 排，`context_recall` 看找全，`context_precision` 看找准。
- 答案再分层：`faithfulness` 看有没有编，`answer_relevancy` 看有没有答对题。
- 选型先抓核心：缺知识用 `RAG`，缺稳定格式用 `Fine-tuning`，缺低成本推理用 `Quantization`。
- Agent 再分工具：`Function Calling` 调工具，`ReAct` 循环决策，`MCP` 标准化接工具。
- 部署最后看场景：低频突发用 `FC`，稳定在线推理用 `PAI-EAS`，`vLLM` 是推理框架不是训练框架。
