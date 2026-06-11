# C2 模拟题多版本输出 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 基于现有 `mock_exam.md` 生成只出题版、答案单独版和计时模拟版三份可直接使用的练习文档。

**Architecture:** 保留现有 15 题主题库不变，以它作为单一事实来源拆分出两个衍生版本；再新增 5 道同范围题目，组合成一份更接近正式考试的 20 题计时模拟版。所有新文件都放在现有 spec 目录下，避免污染仓库其他目录。

**Tech Stack:** Markdown、现有题库文档、手工整理内容

---

### Task 1: 写入实现计划与目标文件列表

**Files:**
- Create: `.trae/specs/generate-c2-mock-exam/implementation-plan-variants.md`
- Read: `.trae/specs/generate-c2-mock-exam/mock_exam.md`

- [ ] **Step 1: 确认输入与输出文件**

输入文件：
- `.trae/specs/generate-c2-mock-exam/mock_exam.md`

输出文件：
- `.trae/specs/generate-c2-mock-exam/mock_exam_questions_only.md`
- `.trae/specs/generate-c2-mock-exam/mock_exam_answers_only.md`
- `.trae/specs/generate-c2-mock-exam/mock_exam_timed_full.md`

- [ ] **Step 2: 锁定版本边界**

版本规则：
- 只出题版：保留题干与选项，不保留答案、解析和来源映射
- 答案单独版：按题号列出答案、解析、课程映射、考纲映射
- 计时模拟版：复用现有 15 题，追加 5 道新题，并加入考试说明、建议时长、答题记录区

### Task 2: 生成只出题版与答案单独版

**Files:**
- Read: `.trae/specs/generate-c2-mock-exam/mock_exam.md`
- Create: `.trae/specs/generate-c2-mock-exam/mock_exam_questions_only.md`
- Create: `.trae/specs/generate-c2-mock-exam/mock_exam_answers_only.md`

- [ ] **Step 1: 生成只出题版**

内容要求：
- 保留题号、题干、选项
- 保留单选 / 多选 / 场景题三个分区
- 增加“使用方法”与“作答建议”

- [ ] **Step 2: 生成答案单独版**

内容要求：
- 每题按题号对应答案
- 补充原题型标记，方便对照
- 保留解析、课程映射、考纲映射

### Task 3: 生成计时模拟版

**Files:**
- Read: `.trae/specs/generate-c2-mock-exam/mock_exam.md`
- Create: `.trae/specs/generate-c2-mock-exam/mock_exam_timed_full.md`

- [ ] **Step 1: 复用现有 15 题**

内容要求：
- 沿用现有题目的知识范围
- 统一改成正式模拟考试文案
- 在题目前加入答题卡与时间说明

- [ ] **Step 2: 新增 5 道题**

新增题要求：
- 仍限定在 C2 与 ACP 大纲范围
- 保持与现有题风格一致
- 优先补充 API 参数、Prompt 稳定性、召回优化、评测闭环等高频点

### Task 4: 校对与交付

**Files:**
- Verify: `.trae/specs/generate-c2-mock-exam/mock_exam_questions_only.md`
- Verify: `.trae/specs/generate-c2-mock-exam/mock_exam_answers_only.md`
- Verify: `.trae/specs/generate-c2-mock-exam/mock_exam_timed_full.md`

- [ ] **Step 1: 校对结构**

检查项：
- 三个文件标题、说明、分区清晰
- 题号连续
- 只出题版不泄露答案

- [ ] **Step 2: 校对内容**

检查项：
- 答案单独版与原题库题号一致
- 计时模拟版总题数为 20
- 新增 5 题不越出 C2 范围

- [ ] **Step 3: 运行 Markdown 诊断**

检查文件：
- `file:///Users/admin/openSource/aliyun_acp_learning/.trae/specs/generate-c2-mock-exam/mock_exam_questions_only.md`
- `file:///Users/admin/openSource/aliyun_acp_learning/.trae/specs/generate-c2-mock-exam/mock_exam_answers_only.md`
- `file:///Users/admin/openSource/aliyun_acp_learning/.trae/specs/generate-c2-mock-exam/mock_exam_timed_full.md`
