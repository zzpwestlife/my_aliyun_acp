# C2 题目质量升级 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将 `exam_materials/C2` 升级为一套高质量样板材料，让 `考试大纲.md`、`模拟题题目.md`、`模拟题答案解析.md` 在考纲分层、题目难度和解析复盘上完全对齐。

**Architecture:** 先重构 `考试大纲.md`，把知识模块、考核层级与命题难度映射写清楚；再基于该映射重写 `模拟题题目.md` 为 `18` 题梯度试卷；最后同步重写 `模拟题答案解析.md`，为每道题补齐标准答案、解析、知识点和映射字段。整个过程只改 `C2` 三个文件，不触碰 `C3/C4` 与 `common/`。

**Tech Stack:** Markdown，现有 `exam_materials/C2` 材料，手工结构校验，`python3` 文本计数校验

---

### Task 1: 重构 C2 考试大纲，建立命题分层基线

**Files:**
- Modify: `/Users/admin/openSource/aliyun_acp_learning/exam_materials/C2/考试大纲.md`

- [ ] **Step 1: 重写文档头部，明确试点目标和命题用途**

将文件开头替换为下面结构：

```md
# C2 考试大纲

本文档用于支撑 `C2` 模块题库重构，不仅整理原考试大纲，还明确每类考点适合出的题型和难度层级，作为 `模拟题题目.md` 与 `模拟题答案解析.md` 的命题基线。

## 一、模块定位与权重

- 模块名称：C2 构造问答系统
- 对应大纲板块：大模型应用开发、提示词工程、大模型检索增强
- 模块特征：权重高、实操性强、既考基础概念也考 RAG 工程化判断
```

- [ ] **Step 2: 把现有考点矩阵重构为“模块 -> 考点 -> 考核层级 -> 命题难度映射”**

在正文中使用如下表头格式，覆盖三个核心模块：

```md
| 模块 | 考点 | 考核层级 | 建议难度 | 常见命题方式 |
| --- | --- | --- | --- | --- |
| 大模型应用开发 | `temperature`、`top_p`、`stream` 参数作用 | 掌握 | 基础 | 参数对比、场景选型 |
| 大模型应用开发 | 多轮对话中的消息历史维护 | 掌握/应用 | 基础/中档 | 追问场景、上下文丢失诊断 |
| 提示词工程 | 系统提示词、分隔符、模板设计 | 掌握/应用 | 基础/中档 | 提示词作用区分、模板选型 |
| RAG 基础 | 解析 -> 切片 -> 召回 -> 重排序 | 掌握 | 基础 | 流程顺序、环节职责 |
| RAG 优化 | 句子窗口检索、标题改写、表格增强 | 应用 | 中档/拔高 | 方法比较、优化优先级 |
| 自动化评测 | RAGAS、评测样本设计、版本对比 | 熟悉/应用 | 中档/拔高 | 指标理解、迭代决策 |
```

- [ ] **Step 3: 新增“命题难度分布建议”小节，锁定 18 题结构**

在大纲文末加入下列段落：

```md
## 四、命题难度分布建议

- 单选题 `10` 题：基础 `4`、中档 `4`、拔高 `2`
- 多选题 `6` 题：基础 `2`、中档 `3`、拔高 `1`
- 场景题 `2` 题：诊断优化 `1`、评测决策 `1`

## 五、命题约束

- 不出脱离课程边界的冷知识题。
- 不使用明显异维度的弱干扰项。
- 至少一半以上客观题应包含条件、场景或方法比较。
```

- [ ] **Step 4: 运行人工检查，确认每个模块都包含“考核层级 + 建议难度 + 常见命题方式”**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
text = Path('/Users/admin/openSource/aliyun_acp_learning/exam_materials/C2/考试大纲.md').read_text()
for key in ['考核层级', '建议难度', '常见命题方式', '命题难度分布建议', '命题约束']:
    print(key, key in text)
PY
```

Expected:

```text
考核层级 True
建议难度 True
常见命题方式 True
命题难度分布建议 True
命题约束 True
```

- [ ] **Step 5: Commit**

```bash
git add /Users/admin/openSource/aliyun_acp_learning/exam_materials/C2/考试大纲.md
git commit -m "docs: rebuild c2 outline as exam authoring baseline"
```

### Task 2: 重写 C2 模拟题题目，建立 18 题梯度试卷

**Files:**
- Modify: `/Users/admin/openSource/aliyun_acp_learning/exam_materials/C2/模拟题题目.md`

- [ ] **Step 1: 重写考试说明，明确题量、梯度和适用方式**

将文档头部替换为下面结构：

```md
# C2 模拟题题目

## 考试说明

- 本卷为 `C2` 质量升级试点卷，共 `18` 题。
- 单选题 `10` 题，多选题 `6` 题，场景题 `2` 题。
- 难度结构：基础题、中档题、拔高题混合分布。
- 建议时长：`45` 到 `55` 分钟。
- 建议先独立完成，再对照 `模拟题答案解析.md` 复盘。
```

- [ ] **Step 2: 重写单选题为 10 题，按 4 / 4 / 2 梯度分布**

将现有单选题整体替换为新的 10 题结构，并保证题号连续。每道题遵循下面格式：

```md
### 1. 【基础】某团队希望让客服答疑机器人在事实问答场景下输出更稳定、随机性更低。以下哪项调参方向最合理？

- A. 提高 `temperature`
- B. 降低 `temperature`
- C. 增大 `stream`
- D. 修改 `messages` 的角色名
```

单选题设计要求：

```text
1. 基础题 4 道：参数作用、消息历史、系统提示词、RAG 基础链路
2. 中档题 4 道：提示词设计判断、RAG 优化选型、检索问题诊断、评测指标理解
3. 拔高题 2 道：多因素权衡、优化优先级决策
```

- [ ] **Step 3: 重写多选题为 6 题，按 2 / 3 / 1 梯度分布**

使用下面格式组织多选题：

```md
## 二、多选题

### 11. 【基础】为了让问答机器人更稳定地处理多轮对话，以下哪些做法是合理的？

- A. 保留系统消息与关键历史轮次
- B. 对过长历史做裁剪或摘要
- C. 完全忽略 assistant 历史输出
- D. 保持消息角色结构清晰
```

多选题质量要求：

```text
1. 至少 3 道题带条件或场景前提
2. 正确答案组合不得大量重复同一种模式
3. 不允许出现“4 个选项都像定义摘抄”的题型
```

- [ ] **Step 4: 保留并重写 2 道场景题，改成可评分结构**

把场景题改为固定提示格式：

```md
## 三、场景题

### 17. 场景题：新人答疑机器人命中零碎片段

请按以下结构作答：

1. 问题诊断
2. 优化顺序
3. 每一步的原因
4. 对应课程章节与考纲落点
```

第二题固定围绕“自动化评测如何指导版本迭代”，并要求回答“评什么、怎么比、如何决策”。

- [ ] **Step 5: 重写题型统计和提交答案区**

将文末统计替换为：

```md
## 题型统计

- 单选题：10
- 多选题：6
- 场景题：2
- 总题数：18
```

并保留提交答案区，使其覆盖 1 至 18 题。

- [ ] **Step 6: 用脚本校验题号和总题量**

Run:

```bash
python3 - <<'PY'
import re
from pathlib import Path
text = Path('/Users/admin/openSource/aliyun_acp_learning/exam_materials/C2/模拟题题目.md').read_text()
nums = re.findall(r'^###\\s+(\\d+)\\.', text, flags=re.M)
print('count=', len(nums))
print('first=', nums[0], 'last=', nums[-1])
print('unique=', len(set(nums)) == len(nums))
PY
```

Expected:

```text
count= 18
first= 1 last= 18
unique= True
```

- [ ] **Step 7: Commit**

```bash
git add /Users/admin/openSource/aliyun_acp_learning/exam_materials/C2/模拟题题目.md
git commit -m "docs: rebuild c2 question set with 18-question difficulty ladder"
```

### Task 3: 重写 C2 模拟题答案解析，建立高质量复盘链路

**Files:**
- Modify: `/Users/admin/openSource/aliyun_acp_learning/exam_materials/C2/模拟题答案解析.md`

- [ ] **Step 1: 重写速查表，使其与 18 题新试卷完全一致**

使用下面的头部结构：

```md
# C2 模拟题答案解析

## 使用说明
- 配合 `模拟题题目.md` 使用。
- 建议先独立完成整套题，再统一核对答案与解析。
- 中档题和拔高题优先关注错项分析。

## 标准答案速查表
```

速查表要求：

```text
1. 覆盖 1 至 18 题
2. 客观题和场景题分区显示
3. 不允许保留旧版 15 题答案
```

- [ ] **Step 2: 为 1 至 16 题逐题补齐统一解析字段**

每道客观题都使用以下模板：

```md
### 1. 题干

标准答案：B

解析：说明为什么正确。

错项分析：说明最具迷惑性的错误项为什么不成立。

知识点：参数控制与生成稳定性

课程映射：`2_1_用大模型构建新人答疑机器人.ipynb`

考纲映射：大模型应用开发 -> 参数作用与消息机制
```

要求：

```text
1. 基础题可简洁解释
2. 中档题和拔高题必须加入“错项分析”
3. 解析不能只重复题干原句
```

- [ ] **Step 3: 重写 17 至 18 题场景题标准答案**

场景题答案采用固定评分结构：

```md
### 17. 场景题：……

参考答案：
1. 问题诊断
2. 优化顺序
3. 原因说明
4. 课程与考纲映射

解析：说明为什么这一路径优先。

知识点：……

课程映射：……

考纲映射：……
```

其中：

```text
17 题：重点是“诊断 -> 提示词优化 -> 检索优化 -> 评测闭环”
18 题：重点是“评测目标 -> 对比方法 -> 版本决策”
```

- [ ] **Step 4: 重写文末复习建议，使其呼应新梯度结构**

将结尾改成：

```md
## 考点覆盖与复习建议

- 基础题优先复习参数作用、消息历史、系统提示词、RAG 基础链路。
- 中档题重点复习提示词优化、RAG 召回优化与评测指标理解。
- 拔高题重点复习多因素权衡、优化顺序与版本决策。
```

- [ ] **Step 5: 用脚本校验答案解析题号与题目文件一致**

Run:

```bash
python3 - <<'PY'
import re
from pathlib import Path
q = Path('/Users/admin/openSource/aliyun_acp_learning/exam_materials/C2/模拟题题目.md').read_text()
a = Path('/Users/admin/openSource/aliyun_acp_learning/exam_materials/C2/模拟题答案解析.md').read_text()
q_nums = re.findall(r'^###\\s+(\\d+)\\.', q, flags=re.M)
a_nums = re.findall(r'^###\\s+(\\d+)\\.', a, flags=re.M)
print('question_count=', len(q_nums))
print('answer_count=', len(a_nums))
print('same=', q_nums == a_nums)
PY
```

Expected:

```text
question_count= 18
answer_count= 18
same= True
```

- [ ] **Step 6: Commit**

```bash
git add /Users/admin/openSource/aliyun_acp_learning/exam_materials/C2/模拟题答案解析.md
git commit -m "docs: rebuild c2 answer key with full rationale mapping"
```

### Task 4: 做整套一致性验收，确认 C2 可以作为样板复制

**Files:**
- Modify: `/Users/admin/openSource/aliyun_acp_learning/exam_materials/C2/考试大纲.md`
- Modify: `/Users/admin/openSource/aliyun_acp_learning/exam_materials/C2/模拟题题目.md`
- Modify: `/Users/admin/openSource/aliyun_acp_learning/exam_materials/C2/模拟题答案解析.md`

- [ ] **Step 1: 手工检查大纲与题目覆盖关系**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
outline = Path('/Users/admin/openSource/aliyun_acp_learning/exam_materials/C2/考试大纲.md').read_text()
questions = Path('/Users/admin/openSource/aliyun_acp_learning/exam_materials/C2/模拟题题目.md').read_text()
for key in ['参数', '消息历史', '系统提示词', 'RAG', '句子窗口', '标题改写', '表格增强', 'RAGAS', '评测']:
    print(key, key in outline, key in questions)
PY
```

Expected: 关键考点在大纲和题目中都能找到落点。

- [ ] **Step 2: 手工检查难度梯度是否完整**

确认题面中至少出现以下标签或等价标识：

```text
基础：6 题
中档：7 题
拔高：3 题
场景：2 题
```

注：这里按整套 18 题统计，场景题单独计数，不与基础 / 中档 / 拔高混淆。

- [ ] **Step 3: 检查解析字段完整性**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
text = Path('/Users/admin/openSource/aliyun_acp_learning/exam_materials/C2/模拟题答案解析.md').read_text()
for key in ['标准答案：', '解析：', '知识点：', '课程映射：', '考纲映射：']:
    print(key, text.count(key))
PY
```

Expected: 每个字段都出现多次，且足以覆盖整套试题。

- [ ] **Step 4: 最终人工验收清单**

逐项核对：

```text
1. 是否仍有旧版 15 题残留
2. 是否仍有明显一眼排除的弱干扰项
3. 是否存在脱离课程边界的拔高题
4. 是否有题目与解析映射不一致
5. 是否有大纲考点未落到题目中
```

- [ ] **Step 5: Commit**

```bash
git add /Users/admin/openSource/aliyun_acp_learning/exam_materials/C2/考试大纲.md /Users/admin/openSource/aliyun_acp_learning/exam_materials/C2/模拟题题目.md /Users/admin/openSource/aliyun_acp_learning/exam_materials/C2/模拟题答案解析.md
git commit -m "docs: finalize c2 as high-quality exam pack pilot"
```
