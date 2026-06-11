# 客观题版与错题分析包 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 新增一套贴近真实 ACP 考试的客观题资料包，只保留单选与多选，并为用户本次作答生成可复用的错题分析文档。

**Architecture:** 保留现有完整题库不动，以现有 15 题中的 1-13 题作为客观题单一事实来源，拆分出“客观题版题目”和“客观题版答案”两份新文件；再新增一份错题分析文档，记录用户本次作答、唯一客观错题、第 12 题的具体错因，以及后续复习建议。整个实现只新增文件，不回写原始题库。

**Tech Stack:** Markdown、现有题库文档、手工整理的错题分析

---

### Task 1: 生成客观题版题目文件

**Files:**
- Read: `.trae/specs/generate-c2-mock-exam/mock_exam_questions_only.md`
- Create: `.trae/specs/generate-c2-mock-exam/mock_exam_objective_only.md`

- [ ] **Step 1: 复制题目骨架并改写说明**

内容要求：
- 标题明确标注“客观题版”
- 顶部说明明确“贴近真实 ACP 考试，仅含单选与多选”
- 保留作答建议，但移除场景题相关提示

- [ ] **Step 2: 保留 1-13 题并移除场景题**

保留范围：
- 单选题 1-8
- 多选题 9-13

移除范围：
- 场景题 14-15
- 原文件中的场景题统计项

- [ ] **Step 3: 更新题型统计**

统计结果应写成：
- 单选题：8
- 多选题：5
- 总题数：13

### Task 2: 生成客观题版答案文件

**Files:**
- Read: `.trae/specs/generate-c2-mock-exam/mock_exam_answers_only.md`
- Create: `.trae/specs/generate-c2-mock-exam/mock_exam_objective_answers.md`

- [ ] **Step 1: 复制答案骨架并改写说明**

内容要求：
- 标题明确标注“客观题答案版”
- 顶部说明明确“仅对应 1-13 题”
- 保留答案、解析、课程映射、考纲映射的固定顺序

- [ ] **Step 2: 保留 1-13 题答案并移除场景题答案**

保留范围：
- 单选题答案 1-8
- 多选题答案 9-13

移除范围：
- 场景题 14-15 的参考答案

### Task 3: 生成错题分析文档

**Files:**
- Create: `.trae/specs/generate-c2-mock-exam/mock_exam_wrong_answer_review.md`
- Reference: `.trae/specs/generate-c2-mock-exam/mock_exam_objective_only.md`
- Reference: `.trae/specs/generate-c2-mock-exam/mock_exam_objective_answers.md`

- [ ] **Step 1: 记录用户本次作答**

记录用户作答：
- 1 B
- 2 C
- 3 A
- 4 C
- 5 B
- 6 B
- 7 B
- 8 C
- 9 ABD
- 10 ABCD
- 11 ABCD
- 12 ACD
- 13 ACD

- [ ] **Step 2: 输出客观题判分结果**

结果要求：
- 总题数：13
- 正确数：12
- 错题数：1
- 正确率：92.3%

- [ ] **Step 3: 写清唯一错题的分析**

第 12 题必须包含：
- 你的答案：ACD
- 标准答案：ABCD
- 漏选项：B 自动合并检索
- 错因：RAG 优化方法集合掌握不完整，能记住句子窗口检索、标题改写、表格增强，但遗漏“自动合并检索”
- 复习落点：`2_5_优化RAG应用提升问答准确度.ipynb`

- [ ] **Step 4: 写出非考试项提示**

说明要求：
- 真实 ACP 考试以单选和多选为主
- 本次原题库中的 14、15 属于延展训练，不计入客观题得分
- 但这两题暴露出用户对“RAG 优化顺序”和“评测闭环”表达不完整

- [ ] **Step 5: 写出下一步复习建议**

建议应至少包含：
- 优先补第 12 题涉及的 RAG 优化方法清单
- 下一轮只刷 13 道客观题
- 再补一轮围绕 RAG 优化与评测的强化题

### Task 4: 校对与验证

**Files:**
- Verify: `.trae/specs/generate-c2-mock-exam/mock_exam_objective_only.md`
- Verify: `.trae/specs/generate-c2-mock-exam/mock_exam_objective_answers.md`
- Verify: `.trae/specs/generate-c2-mock-exam/mock_exam_wrong_answer_review.md`

- [ ] **Step 1: 检查新题库范围**

检查项：
- 只包含 1-13 题
- 不包含场景题
- 标题与说明明确写出“客观题版”

- [ ] **Step 2: 检查错题分析一致性**

检查项：
- 第 12 题是唯一客观错题
- 正确率计算为 12/13
- 不把 14、15 计入客观题成绩

- [ ] **Step 3: 运行 Markdown 诊断**

检查文件：
- `file:///Users/admin/openSource/aliyun_acp_learning/.trae/specs/generate-c2-mock-exam/mock_exam_objective_only.md`
- `file:///Users/admin/openSource/aliyun_acp_learning/.trae/specs/generate-c2-mock-exam/mock_exam_objective_answers.md`
- `file:///Users/admin/openSource/aliyun_acp_learning/.trae/specs/generate-c2-mock-exam/mock_exam_wrong_answer_review.md`
