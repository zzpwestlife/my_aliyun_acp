# 第 12 题课内口径修正 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将第 12 题按 C2_2.5 课内表述统一修正为 A、C、D，并同步更新所有相关题库与错题分析文件。

**Architecture:** 本次为内容一致性修正，不新增功能文件结构。直接修改全仓库中第 12 题相关的题干、答案与错题分析结论，确保所有入口文件口径统一，并把你的客观题成绩改判为 13/13。

**Tech Stack:** Markdown、现有题库文件、手工校对

---

### Task 1: 修正所有题库中的第 12 题选项与答案口径

**Files:**
- Modify: `.trae/specs/generate-c2-mock-exam/mock_exam.md`
- Modify: `.trae/specs/generate-c2-mock-exam/mock_exam_questions_only.md`
- Modify: `.trae/specs/generate-c2-mock-exam/mock_exam_timed_full.md`
- Modify: `.trae/specs/generate-c2-mock-exam/mock_exam_objective_only.md`

- [ ] **Step 1: 修改题目选项**

将第 12 题的选项从：

```md
- A. 句子窗口检索
- B. 自动合并检索
- C. 标题改写优化
- D. 表格内容增强
```

改为：

```md
- A. 句子窗口检索
- B. 提高 temperature
- C. 标题改写优化
- D. 表格内容增强
```

- [ ] **Step 2: 保持题干不变**

第 12 题题干继续保持：

```md
### 12. 以下哪些方法属于 C2 中用于提升 RAG 准确度的策略？
```

### Task 2: 修正所有答案文件中的第 12 题标准答案与解析

**Files:**
- Modify: `.trae/specs/generate-c2-mock-exam/mock_exam_answers_only.md`
- Modify: `.trae/specs/generate-c2-mock-exam/mock_exam_objective_answers.md`
- Modify: `.trae/specs/generate-c2-mock-exam/mock_exam_timed_full.md`

- [ ] **Step 1: 将标准答案统一改为 A、C、D**

把第 12 题答案从：

```md
- 标准答案：A、B、C、D
```

改为：

```md
- 标准答案：A、C、D
```

在计时模拟版的答案区，把：

```md
答案：A、B、C、D
```

改为：

```md
答案：A、C、D
```

- [ ] **Step 2: 修正解析**

把第 12 题解析统一改成：

```md
这些都属于课程中明确出现或可直接归纳出的 RAG 优化能力。提高 temperature 属于模型生成参数调节，不属于 2.5 课内强调的 RAG 检索优化策略。
```

### Task 3: 修正错题分析文档

**Files:**
- Modify: `.trae/specs/generate-c2-mock-exam/mock_exam_wrong_answer_review.md`

- [ ] **Step 1: 修改成绩**

将成绩从：

```md
- 总题数：13
- 正确数：12
- 错题数：1
- 正确率：92.3%
```

改为：

```md
- 总题数：13
- 正确数：13
- 错题数：0
- 正确率：100%
```

- [ ] **Step 2: 删除“第 12 题错题”结论**

删除以下内容：

```md
本次客观题只有 1 道错题：
- 第 12 题：以下哪些方法属于 C2 中用于提升 RAG 准确度的策略？
```

改为：

```md
本次客观题已全部答对。
```

- [ ] **Step 3: 增加口径修正说明**

新增说明：

```md
旧版第 12 题把“自动合并检索”纳入正确项，该表述来自考试大纲扩展口径，但不属于当前 C2_2.5 课内原文的直接表述。本次已按课内口径修正，因此你的原答案 ACD 改判为正确。
```

### Task 4: 校对与验证

**Files:**
- Verify: `.trae/specs/generate-c2-mock-exam/mock_exam.md`
- Verify: `.trae/specs/generate-c2-mock-exam/mock_exam_questions_only.md`
- Verify: `.trae/specs/generate-c2-mock-exam/mock_exam_timed_full.md`
- Verify: `.trae/specs/generate-c2-mock-exam/mock_exam_answers_only.md`
- Verify: `.trae/specs/generate-c2-mock-exam/mock_exam_objective_only.md`
- Verify: `.trae/specs/generate-c2-mock-exam/mock_exam_objective_answers.md`
- Verify: `.trae/specs/generate-c2-mock-exam/mock_exam_wrong_answer_review.md`

- [ ] **Step 1: 搜索残留表述**

运行：

```bash
rg -n "自动合并检索|A、B、C、D|答案：A、B、C、D|标准答案：A、B、C、D" .trae/specs/generate-c2-mock-exam
```

预期：
- 不再在第 12 题相关文件中出现“自动合并检索”作为正确项
- 不再出现旧的第 12 题全选四答案

- [ ] **Step 2: 运行 Markdown 诊断**

检查文件：
- `file:///Users/admin/openSource/aliyun_acp_learning/.trae/specs/generate-c2-mock-exam/mock_exam.md`
- `file:///Users/admin/openSource/aliyun_acp_learning/.trae/specs/generate-c2-mock-exam/mock_exam_questions_only.md`
- `file:///Users/admin/openSource/aliyun_acp_learning/.trae/specs/generate-c2-mock-exam/mock_exam_timed_full.md`
- `file:///Users/admin/openSource/aliyun_acp_learning/.trae/specs/generate-c2-mock-exam/mock_exam_answers_only.md`
- `file:///Users/admin/openSource/aliyun_acp_learning/.trae/specs/generate-c2-mock-exam/mock_exam_objective_only.md`
- `file:///Users/admin/openSource/aliyun_acp_learning/.trae/specs/generate-c2-mock-exam/mock_exam_objective_answers.md`
- `file:///Users/admin/openSource/aliyun_acp_learning/.trae/specs/generate-c2-mock-exam/mock_exam_wrong_answer_review.md`
