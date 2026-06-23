# C3 题目质量升级 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将 `exam_materials/C3` 升级为一套高质量 Agent 模块题库，让 `考试大纲.md`、`模拟题题目.md`、`模拟题答案解析.md` 在命题分层、题目区分度和解析复盘上完全对齐。

**Architecture:** 先把 `考试大纲.md` 改造成命题基线稿，明确 `3.1` 到 `3.7` 各模块的考核层级、建议难度和命题方式；再重写 `模拟题题目.md`，保留 `20` 题全客观题结构，但重构基础、中档、拔高梯度；最后同步重写 `模拟题答案解析.md`，为每题补齐标准答案、解析、错项分析、知识点和考纲映射，并做一致性校验。

**Tech Stack:** Markdown，现有 `exam_materials/C3` 材料，`python3` 文本校验脚本，人工题目质量复核

---

### Task 1: 重构 C3 考试大纲，建立 Agent 模块命题基线

**Files:**
- Modify: `/Users/admin/openSource/aliyun_acp_learning/exam_materials/C3/考试大纲.md`

- [ ] **Step 1: 重写文档头部，明确 C3 的命题定位**

将文档开头替换为以下结构：

```md
# C3 考试大纲

本文档用于支撑 `C3` 模块题库升级，不仅整理《阿里云大模型 ACP 考试大纲》中与“构建 Agent 系统”相关的核心要求，也明确每类考点适合出的题型和难度层级，作为 `模拟题题目.md` 与 `模拟题答案解析.md` 的命题基线。

## 一、模块定位与权重

- 模块名称：`C3 构建 Agent 系统`
- 对应教程：`3_1` 到 `3_7`
- 对应考试大纲板块：多 Agent 及多模态应用
- 模块特征：更强调机制边界、模式选择、组合能力设计和评测闭环
```

- [ ] **Step 2: 将正文改造成“模块 -> 考点 -> 考核层级 -> 建议难度 -> 常见命题方式”矩阵**

正文必须覆盖以下模块，并统一使用这个表头：

```md
| 模块 | 考点 | 考核层级 | 建议难度 | 常见命题方式 |
| --- | --- | --- | --- | --- |
| Agent 运行机制与工具调用 | 结构化输出、外部执行、工具调用边界 | 掌握 | 基础 / 中档 | 运行机制、工具接入选择 |
| 工作流、规划与反思 | 固定工作流、Plan & Execute、自我反馈、外部反馈 | 理解 / 应用 | 中档 | 任务类型匹配、反思策略判断 |
| 多 Agent 协作 | Leader-Worker、Blackboard、handoff | 掌握 / 应用 | 中档 / 拔高 | 协作模式选型 |
| 记忆管理 | 无状态、截断、摘要、向量召回、主动记忆 | 理解 / 应用 | 基础 / 中档 | 记忆策略组合 |
| Skill 设计与沉淀 | Prompt 到 Skill 的演进、版本化、资源组织 | 理解 / 应用 | 基础 / 中档 | 复用能力设计 |
| 评测驱动开发 | 端到端评测、白盒评测、持续闭环 | 掌握 / 应用 | 中档 / 拔高 | 诊断与迭代判断 |
| Qwen Code 实践 | Plan Mode、上下文管理、EPCC 工作流 | 熟悉 / 应用 | 基础 / 中档 | 开发方式与方法论联系 |
```

- [ ] **Step 3: 新增“命题难度分布建议”和“易错方向”**

在文末加入：

```md
## 三、命题难度分布建议

- 单选题 `12`：基础 `5`、中档 `5`、拔高 `2`
- 多选题 `8`：基础 `3`、中档 `3`、拔高 `2`

## 四、易错方向

- 把工具调用误解为模型直接执行工具。
- 把固定工作流、自主规划、反思机制混为一谈。
- 只记多 Agent 模式名称，不会判断适用场景。
- 只知道有记忆、Skill、评测，但不会组合成可持续迭代系统。
```

- [ ] **Step 4: 用脚本检查大纲是否包含关键字段和模块**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
text = Path('/Users/admin/openSource/aliyun_acp_learning/exam_materials/C3/考试大纲.md').read_text()
for key in ['考核层级', '建议难度', '常见命题方式', '命题难度分布建议', '易错方向', 'Qwen Code']:
    print(key, key in text)
PY
```

Expected:

```text
考核层级 True
建议难度 True
常见命题方式 True
命题难度分布建议 True
易错方向 True
Qwen Code True
```

- [ ] **Step 5: Commit**

```bash
git add /Users/admin/openSource/aliyun_acp_learning/exam_materials/C3/考试大纲.md
git commit -m "docs: rebuild c3 outline as agent exam authoring baseline"
```

### Task 2: 重写 C3 模拟题题目，保留全客观题但提升区分度

**Files:**
- Modify: `/Users/admin/openSource/aliyun_acp_learning/exam_materials/C3/模拟题题目.md`

- [ ] **Step 1: 重写考试说明，锁定 20 题与难度梯度**

将文档头部改成：

```md
# C3 模拟题题目

## 考试说明

- 本卷为 `C3` 质量升级试点卷，共 `20` 题。
- 单选题 `12` 题，多选题 `8` 题。
- 难度结构：基础题 `8`、中档题 `8`、拔高题 `4`。
- 建议时长：`45` 到 `55` 分钟。
- 建议先独立作答，再对照 `模拟题答案解析.md` 复盘。
```

- [ ] **Step 2: 重写 12 道单选题，确保“基础 / 中档 / 拔高”分布清晰**

单选题按以下主题重写：

```text
1-3: Agent 运行机制与工具调用
4-5: 工作流、规划与反思
6-7: 多 Agent 协作模式
8-9: 记忆管理
10: Skill
11: 评测驱动
12: 综合拔高题
```

每题采用如下格式：

```md
### 1. 【基础·3.1】题干……

- A. …
- B. …
- C. …
- D. …
```

并满足：

```text
1. 至少 6 道单选题带明确场景前提
2. 至少 4 道单选题体现模式比较或方法选择
3. 不允许出现明显送分干扰项
```

- [ ] **Step 3: 重写 8 道多选题，降低“全选型”重复率**

多选题按以下主题设计：

```text
13: 工具调用可靠性
14: 工作流与反思
15: 多 Agent 协作
16: 记忆管理
17: Skill 设计
18: 评测驱动
19: Qwen Code 实践
20: 综合能力组合
```

要求：

```text
1. 正确答案组合不得大量重复 ABCD
2. 至少 4 道多选题含条件或限制前提
3. 综合题要考“完整性”而不只是“概念罗列”
```

- [ ] **Step 4: 调整作答建议和题型统计**

将文末更新为：

```md
## 题型统计

- 单选题：12
- 多选题：8
- 总题数：20
```

作答建议需改成围绕“工具、规划、协作、记忆、Skill、评测、Qwen Code”七个维度判断。

- [ ] **Step 5: 用脚本检查题号和总题量**

Run:

```bash
python3 - <<'PY'
import re
from pathlib import Path
text = Path('/Users/admin/openSource/aliyun_acp_learning/exam_materials/C3/模拟题题目.md').read_text()
nums = re.findall(r'^###\\s+(\\d+)\\.', text, flags=re.M)
print('count=', len(nums))
print('first=', nums[0], 'last=', nums[-1])
print('unique=', len(set(nums)) == len(nums))
PY
```

Expected:

```text
count= 20
first= 1 last= 20
unique= True
```

- [ ] **Step 6: Commit**

```bash
git add /Users/admin/openSource/aliyun_acp_learning/exam_materials/C3/模拟题题目.md
git commit -m "docs: rebuild c3 objective exam with stronger design judgment"
```

### Task 3: 重写 C3 模拟题答案解析，建立高质量复盘链路

**Files:**
- Modify: `/Users/admin/openSource/aliyun_acp_learning/exam_materials/C3/模拟题答案解析.md`

- [ ] **Step 1: 重写速查表，保持与 20 题新试卷完全同步**

文档头部统一为：

```md
# C3 模拟题答案解析

## 使用说明
- 配合 `模拟题题目.md` 使用。
- 建议先完整作答，再结合速查表和逐题解析复盘。
- 中档题和拔高题优先看“错项分析”和“系统设计判断依据”。

## 标准答案速查表
```

速查表要求：

```text
1. 覆盖 1 至 20 题
2. 单选与多选分布清晰
3. 不能保留旧题答案组合
```

- [ ] **Step 2: 为 1 至 20 题统一补齐解析字段**

每题使用如下模板：

```md
### 1. 题干

标准答案：B

解析：说明为什么正确。

错项分析：说明最关键错项为什么不成立。

知识点：……

考纲映射：……
```

要求：

```text
1. 基础题也要有错项分析，但可更简洁
2. 中档与拔高题必须解释“为什么这个模式 / 组合更优”
3. 综合题要指出其他能力组合缺了什么
```

- [ ] **Step 3: 重写文末“考点覆盖与复习建议”**

将结尾改成：

```md
## 考点覆盖与复习建议

- 先复习 Agent 运行机制、工具调用与工作流选择。
- 再复习多 Agent 协作、记忆管理和 Skill 沉淀。
- 最后复习评测驱动和 Qwen Code 方法论，把多个能力串成闭环。
```

- [ ] **Step 4: 用脚本校验解析题号与题面一致**

Run:

```bash
python3 - <<'PY'
import re
from pathlib import Path
q = Path('/Users/admin/openSource/aliyun_acp_learning/exam_materials/C3/模拟题题目.md').read_text()
a = Path('/Users/admin/openSource/aliyun_acp_learning/exam_materials/C3/模拟题答案解析.md').read_text()
q_nums = re.findall(r'^###\\s+(\\d+)\\.', q, flags=re.M)
a_nums = re.findall(r'^###\\s+(\\d+)\\.', a, flags=re.M)
print('question_count=', len(q_nums))
print('answer_count=', len(a_nums))
print('same=', q_nums == a_nums)
PY
```

Expected:

```text
question_count= 20
answer_count= 20
same= True
```

- [ ] **Step 5: Commit**

```bash
git add /Users/admin/openSource/aliyun_acp_learning/exam_materials/C3/模拟题答案解析.md
git commit -m "docs: rebuild c3 answer key with rationale and mapping"
```

### Task 4: 做 C3 整套一致性验收，确认可作为 Agent 模块样板

**Files:**
- Modify: `/Users/admin/openSource/aliyun_acp_learning/exam_materials/C3/考试大纲.md`
- Modify: `/Users/admin/openSource/aliyun_acp_learning/exam_materials/C3/模拟题题目.md`
- Modify: `/Users/admin/openSource/aliyun_acp_learning/exam_materials/C3/模拟题答案解析.md`

- [ ] **Step 1: 检查核心考点是否均已落题**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
outline = Path('/Users/admin/openSource/aliyun_acp_learning/exam_materials/C3/考试大纲.md').read_text()
questions = Path('/Users/admin/openSource/aliyun_acp_learning/exam_materials/C3/模拟题题目.md').read_text()
for key in ['工具调用', 'Plan & Execute', 'Blackboard', '记忆', 'Skill', '评测', 'Qwen Code']:
    print(f'{key}: outline={key in outline}, questions={key in questions}')
PY
```

Expected: 关键主题在大纲和题面中都能找到落点。

- [ ] **Step 2: 检查难度梯度与题型分布**

人工核对：

```text
1. 基础题约 8 道
2. 中档题约 8 道
3. 拔高题约 4 道
4. 单选 12 道
5. 多选 8 道
```

- [ ] **Step 3: 检查解析字段完整性**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
text = Path('/Users/admin/openSource/aliyun_acp_learning/exam_materials/C3/模拟题答案解析.md').read_text()
for key in ['标准答案：', '解析：', '错项分析：', '知识点：', '考纲映射：']:
    print(key, text.count(key))
PY
```

Expected: 每个字段都出现多次，足以覆盖全部 20 题。

- [ ] **Step 4: 最终人工验收清单**

逐项核对：

```text
1. 是否仍保留旧版偏知识点摘抄的题目
2. 是否仍有明显一眼排除的弱干扰项
3. 是否存在多选题大量重复 ABCD 的情况
4. 是否有解析缺少错项分析
5. 是否有大纲中的核心模块未在题目中体现
```

- [ ] **Step 5: Commit**

```bash
git add /Users/admin/openSource/aliyun_acp_learning/exam_materials/C3/考试大纲.md /Users/admin/openSource/aliyun_acp_learning/exam_materials/C3/模拟题题目.md /Users/admin/openSource/aliyun_acp_learning/exam_materials/C3/模拟题答案解析.md
git commit -m "docs: finalize c3 as high-quality agent exam pack pilot"
```
