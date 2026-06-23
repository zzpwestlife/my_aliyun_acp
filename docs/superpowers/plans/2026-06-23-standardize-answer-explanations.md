# 模拟题答案解析统一模板 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 统一 `C2`、`C3`、`C4` 三份 `模拟题答案解析.md` 的结构与排版，采用“标准答案速查表 + 逐题答案解析 + 知识点/考纲映射”的标准考试复盘格式。

**Architecture:** 保留每章现有题目内容与知识点映射，不新增题目，只做文档重组与版式统一。先定义统一模板，再逐章套用，最后做目录级核查，确保三份文件的章节顺序、标题层级、题目区块字段和术语完全一致。

**Tech Stack:** Markdown，仓库内现有题库文件，人工结构化校验

---

### Task 1: 定义统一答案解析模板

**Files:**
- Create: `docs/superpowers/plans/2026-06-23-standardize-answer-explanations.md`
- Modify: `exam_materials/C2/模拟题答案解析.md`
- Modify: `exam_materials/C3/模拟题答案解析.md`
- Modify: `exam_materials/C4/模拟题答案解析.md`

- [ ] **Step 1: 确认统一标题结构**

```md
# [章节编号] 模拟题答案解析

## 使用说明
- 说明本文件的用途、建议使用方式与适用范围。

## 标准答案速查表
- 用表格按题号给出标准答案。

## 一、单选题答案解析
- 每题固定为：题号与题干 / 标准答案 / 解析 / 知识点 / 考纲映射。

## 二、多选题答案解析
- 每题固定为：题号与题干 / 标准答案 / 解析 / 知识点 / 考纲映射。

## 考点覆盖与复习建议
- 总结本章覆盖范围、薄弱点和复习建议。
```

- [ ] **Step 2: 明确逐题区块模板**

```md
### 1. 题干

标准答案：A

解析：……

知识点：……

考纲映射：……
```

- [ ] **Step 3: 统一字段约束**

```text
1. 不保留“题型：单选题/多选题”这类重复字段。
2. 不保留“改进对照总结”“设计原则”这类面向出题过程的说明。
3. 允许保留课程映射信息，但若存在，与“知识点/考纲映射”并列，不替代二者。
4. 速查表必须放在逐题解析之前。
5. 单选题与多选题分区顺序固定，不插入其他章节。
```

- [ ] **Step 4: 人工检查模板是否覆盖三章现状**

Run: `手工对照 exam_materials/C2/模拟题答案解析.md exam_materials/C3/模拟题答案解析.md exam_materials/C4/模拟题答案解析.md`
Expected: 三份文件都能映射到同一模板，且不需要删减题目本身。

- [ ] **Step 5: Commit**

```bash
git add docs/superpowers/plans/2026-06-23-standardize-answer-explanations.md
git commit -m "docs: add answer explanation formatting plan"
```

### Task 2: 重构 C2 答案解析版式

**Files:**
- Modify: `exam_materials/C2/模拟题答案解析.md`

- [ ] **Step 1: 调整文件头部为统一说明 + 速查表**

```md
# C2 模拟题答案解析

## 使用说明
- 配合 `模拟题题目.md` 使用。
- 建议先完整作答，再核对答案与解析。
- 优先结合“知识点”和“考纲映射”回看薄弱项。

## 标准答案速查表
| 题号 | 答案 |
| --- | --- |
| 1 | B |
| 2 | C |
| 3 | A |
```

- [ ] **Step 2: 将现有“单选题答案/多选题答案/场景题参考答案”统一改成解析分区**

```md
## 一、单选题答案解析
## 二、多选题答案解析
## 三、场景题参考答案
```

Expected: `C2` 保留场景题分区，但前两区标题改为“答案解析”，与标准模板一致。

- [ ] **Step 3: 删除逐题内重复字段，保留核心信息**

```md
### 1. 在调用大模型生成答复时，以下哪个参数最直接影响输出的随机性？

标准答案：B

解析：`temperature` 用于调节采样随机性……

知识点：大模型应用开发参数控制

课程映射：`2_1_用大模型构建新人答疑机器人.ipynb`

考纲映射：大模型应用开发 -> 基本 API 参数如 `model`、`temperature`、`top_p`
```

- [ ] **Step 4: 增加结尾复习建议**

```md
## 考点覆盖与复习建议
- 重点回看 RAG 基础链路、RAG 优化与自动化评测。
- 对错题优先按“应用开发 -> 提示词 -> RAG -> 评测”的顺序复盘。
```

- [ ] **Step 5: 手工检查题号连续、速查表与逐题答案一致**

Run: `手工核对 C2 全部题号、答案字母、章节标题`
Expected: 速查表答案与逐题答案完全一致，无重复题号，无缺失字段。

- [ ] **Step 6: Commit**

```bash
git add exam_materials/C2/模拟题答案解析.md
git commit -m "docs: standardize c2 answer explanation format"
```

### Task 3: 重构 C3 答案解析版式

**Files:**
- Modify: `exam_materials/C3/模拟题答案解析.md`

- [ ] **Step 1: 用统一结构替换现有“说明/作答建议/课程章节到考纲映射概览”的头部组织**

```md
# C3 模拟题答案解析

## 使用说明
- 配合 `模拟题题目.md` 使用。
- 适用于按章节刷题和整章复盘。

## 标准答案速查表
| 题号 | 答案 | 题号 | 答案 |
| --- | --- | --- | --- |
| 1 | B | 11 | B |
| 2 | B | 12 | A |
```

Expected: “课程章节到考纲映射概览”中的关键信息迁移到文末“考点覆盖与复习建议”，不再作为头部大表格保留。

- [ ] **Step 2: 把逐题内容统一为标准字段顺序**

```md
### 1. 【基础·3.1】……

标准答案：B

解析：……

知识点：3.1 工具调用机制——结构化输出与外部执行分离

考纲映射：智能体与应用 -> 理解智能体运行机制
```

- [ ] **Step 3: 去掉“---”分隔线和冗余组合说明，保留考试复盘需要的信息**

```text
删除：
1. 题目之间单独的分隔线 `---`
2. “组合：ABC，保留原组合” 这类出题过程描述
3. “改进对照总结” 这类元说明
```

- [ ] **Step 4: 新增结尾复习建议区**

```md
## 考点覆盖与复习建议
- 重点覆盖 3.1-3.7 工具、规划、协作、记忆、Skill、评测、Qwen Code。
- 复习时优先区分“单 Agent 能力边界”和“多 Agent 组织方式”。
```

- [ ] **Step 5: 手工检查 20 道题的速查表与逐题答案一致**

Run: `手工核对 C3 题号 1-20 的答案映射`
Expected: 速查表与逐题答案完全一致，文档内不再出现出题设计过程说明。

- [ ] **Step 6: Commit**

```bash
git add exam_materials/C3/模拟题答案解析.md
git commit -m "docs: standardize c3 answer explanation format"
```

### Task 4: 重构 C4 答案解析版式

**Files:**
- Modify: `exam_materials/C4/模拟题答案解析.md`

- [ ] **Step 1: 把现有速查表上移到使用说明后，作为文首速查区**

```md
# C4 模拟题答案解析

## 使用说明
- 配合 `模拟题题目.md` 使用。
- 建议先完成整套题，再使用速查表快速定位错题。

## 标准答案速查表
| 题号 | 答案 | 题号 | 答案 | 题号 | 答案 | 题号 | 答案 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B | 9 | B | 17 | C | 25 | ACD |
```

- [ ] **Step 2: 保留单选/多选两大题区，但去掉头部的设计性说明**

```text
删除：
1. “设计原则”
2. “作答建议”
3. “课程章节到考纲映射概览”大表
保留：
1. 单选题逐题解析
2. 多选题逐题解析
3. 知识点与考纲映射
```

- [ ] **Step 3: 统一逐题格式并保持题号连续**

```md
### 19. 【中档·4.1】关于蒸馏训练数据构建流程，以下哪些做法合理？

标准答案：ABC

解析：A、B、C是完整流水线中的合理动作……

知识点：4.1 数据构建流程

考纲映射：模型定制与优化
```

- [ ] **Step 4: 用文末复习建议替代现有“考点覆盖检查”口径**

```md
## 考点覆盖与复习建议
- 覆盖 `4.1-4.4` 全章，重点包括蒸馏边界、部署选型、生产实践、安全合规。
- 复习时优先区分“模型能力问题”“部署治理问题”“安全控制问题”三类失分来源。
```

- [ ] **Step 5: 手工检查 32 道题的速查表与逐题答案一致**

Run: `手工核对 C4 题号 1-32 的答案映射`
Expected: 速查表与逐题答案完全一致，且头部结构与 C2/C3 保持一致。

- [ ] **Step 6: Commit**

```bash
git add exam_materials/C4/模拟题答案解析.md
git commit -m "docs: standardize c4 answer explanation format"
```

### Task 5: 目录级一致性核查

**Files:**
- Modify: `exam_materials/README.md`
- Test: `exam_materials/C2/模拟题答案解析.md`
- Test: `exam_materials/C3/模拟题答案解析.md`
- Test: `exam_materials/C4/模拟题答案解析.md`

- [ ] **Step 1: 更新总索引中的答案解析说明**

```md
## 模拟题
- `C2/模拟题答案解析.md`：含标准答案速查表、逐题解析、知识点与考纲映射。
- `C3/模拟题答案解析.md`：含标准答案速查表、逐题解析、知识点与考纲映射。
- `C4/模拟题答案解析.md`：含标准答案速查表、逐题解析、知识点与考纲映射。
```

- [ ] **Step 2: 核查三份文件标题与章节顺序一致**

Run: `手工核对三份文件均包含“使用说明 -> 标准答案速查表 -> 单选题答案解析 -> 多选题答案解析 -> 考点覆盖与复习建议”`
Expected: 三份文件都符合统一结构；`C2` 可额外保留“场景题参考答案”分区。

- [ ] **Step 3: 核查字段一致性**

```text
每道题至少包含：
1. 标准答案
2. 解析
3. 知识点
4. 考纲映射
```

- [ ] **Step 4: 最终检查无多余过程性说明残留**

Run: `手工搜索“改进对照总结”“设计原则”“保留原组合”“题型：”等词`
Expected: 这些面向出题过程或重复字段的内容不再出现在最终答案解析文件中。

- [ ] **Step 5: Commit**

```bash
git add exam_materials/README.md exam_materials/C2/模拟题答案解析.md exam_materials/C3/模拟题答案解析.md exam_materials/C4/模拟题答案解析.md
git commit -m "docs: unify answer explanation documents"
```
