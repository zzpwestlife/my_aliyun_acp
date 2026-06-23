# 扩充 C2 C3 C4 题库 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 把 `exam_materials/C2`、`C3`、`C4` 三个模块的现有题库直接扩充到目标规模，并保持不重复、不换皮、解析字段完整。

**Architecture:** 本次不新增文件、不拆分卷别，也不重排旧题号，只在现有 `模拟题题目.md` 与 `模拟题答案解析.md` 中继续追加。执行顺序按模块分三段推进：先盘点现有覆盖与题号边界，再追加新题，最后同步答案解析与全量校验，确保题目数量、题号连续性、速查表与解析一一对应。

**Tech Stack:** Markdown 文档编辑、ripgrep 题号统计、VS Code diagnostics、本地命令行校验

---

### Task 1: 盘点现有题库边界与新增缺口

**Files:**
- Modify: `docs/superpowers/plans/2026-06-23-expand-c2-c3-c4-question-bank.md`
- Read: `exam_materials/C2/模拟题题目.md`
- Read: `exam_materials/C2/模拟题答案解析.md`
- Read: `exam_materials/C3/模拟题题目.md`
- Read: `exam_materials/C3/模拟题答案解析.md`
- Read: `exam_materials/C4/模拟题题目.md`
- Read: `exam_materials/C4/模拟题答案解析.md`

- [ ] **Step 1: 记录每个模块当前题量与目标题量**

在计划执行日志中先写出目标表，避免后续追加时算错数量：

```text
C2 当前：单选 10，多选 6，场景 2
C2 目标：单选 18，多选 10，场景 2（场景题不再扩）
C2 新增：单选 +8，多选 +4

C3 当前：单选 12，多选 8
C3 目标：单选 16，多选 10
C3 新增：单选 +4，多选 +2

C4 当前：单选 18，多选 14
C4 目标：单选 24，多选 14
C4 新增：单选 +6，多选 +0（保留现有 14 道多选，不删旧题）
```

- [ ] **Step 2: 先核对规格与现状是否冲突**

运行：

```bash
python3 - <<'PY'
from pathlib import Path
files = {
    "C2": Path("/Users/admin/openSource/aliyun_acp_learning/exam_materials/C2/模拟题题目.md"),
    "C3": Path("/Users/admin/openSource/aliyun_acp_learning/exam_materials/C3/模拟题题目.md"),
    "C4": Path("/Users/admin/openSource/aliyun_acp_learning/exam_materials/C4/模拟题题目.md"),
}
for name, path in files.items():
    text = path.read_text()
    single = text.count("### ") if name == "C2" else 0
    print(name, "loaded", len(text))
PY
```

Expected:

```text
脚本能成功读取三个文件，不报路径错误。
```

说明：这里不是依赖脚本最终计数，而是先确认文件可读；真正计数在下一步用更直接方式做。

- [ ] **Step 3: 用标题边界人工确认最后题号**

逐个确认当前最后题号，作为追加起点：

```text
C2 题目文件最后题号应为 18
C3 题目文件最后题号应为 20
C4 题目文件最后题号应为 32
```

并记录追加规则：

```text
C2 新单选从 19 开始，新多选从 27 开始
C3 新单选从 21 开始，新多选从 25 开始
C4 新单选从 33 开始；现有多选 19-32 保持不变
```

- [ ] **Step 4: 形成模块级新增覆盖清单**

执行前先写出每个模块的新题覆盖角度，防止换皮：

```text
C2 新增角度：
1. Query 改写与召回鲁棒性
2. chunk size / overlap 取舍
3. 重排序与召回阶段职责边界
4. 表格增强的适用场景
5. RAGAS 或自动评测指标理解
6. 拒答与证据约束组合策略
7. 检索失败时的优先排查顺序
8. 提示词、检索、评测三者联动

C3 新增角度：
1. 工具选择与工具滥用边界
2. 手工工作流与 Agent 自主规划边界
3. handoff / Leader-Worker / Blackboard 的误用场景
4. 长短期记忆协同
5. Skill 与普通 Prompt 的边界
6. 白盒评测与端到端评测组合

C4 新增角度：
1. 蒸馏数据分布与长尾覆盖
2. 线上部署迁移路径
3. 成本、TTFT、吞吐之间的取舍
4. 缓存与批处理适用边界
5. 护栏、鉴权、审计的职责边界
6. 写操作工具的上线治理
```

- [ ] **Step 5: 提交或标记检查点**

Run:

```bash
git status --short
```

Expected:

```text
允许看到现有题库文件的在制改动，但本轮不应额外重排旧题号。
```

---

### Task 2: 扩充 C2 题目与答案解析

**Files:**
- Modify: `exam_materials/C2/模拟题题目.md`
- Modify: `exam_materials/C2/模拟题答案解析.md`

- [ ] **Step 1: 在 `模拟题题目.md` 中追加 8 道单选题**

新增单选必须在不改旧题号的前提下向后追加，因此题号改为：

```text
1-10 旧单选保留
11-16 旧多选保留
17-18 旧场景题保留
19-26 新单选
27-30 新多选
```

新增单选题要求：

```text
至少 3 题考 RAG 检索链路边界
至少 2 题考评测或评估设计
至少 2 题考提示词与结构化输出
至少 1 题考优化优先级
```

- [ ] **Step 2: 在 `模拟题题目.md` 中追加 4 道多选题并更新提交答案区**

新增多选直接从 `27-30` 追加，并同步更新提交答案区：

```markdown
## 提交答案区

| 题号 | 答案 | 题号 | 答案 | 题号 | 答案 | 题号 | 答案 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ___ | 9 | ___ | 17 | ___ | 25 | ___ |
| 2 | ___ | 10 | ___ | 18 | ___ | 26 | ___ |
| 3 | ___ | 11 | ___ | 19 | ___ | 27 | ___ |
| 4 | ___ | 12 | ___ | 20 | ___ | 28 | ___ |
| 5 | ___ | 13 | ___ | 21 | ___ | 29 | ___ |
| 6 | ___ | 14 | ___ | 22 | ___ | 30 | ___ |
| 7 | ___ | 15 | ___ | 23 | ___ |  |  |
| 8 | ___ | 16 | ___ | 24 | ___ |  |  |
```

并把统计区更新为：

```markdown
- 单选题：18
- 多选题：10
- 场景题：2
- 总题数：30
```

- [ ] **Step 3: 同步重写 `模拟题答案解析.md` 的速查表**

速查表必须覆盖 `1-30` 全部题号，并保留场景题关键词表。格式参考：

```markdown
### 客观题

| 题号 | 答案 | 题号 | 答案 | 题号 | 答案 | 题号 | 答案 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B | 9 | C | 17 | 关键词 | 25 | B |
| 2 | C | 10 | A | 18 | 关键词 | 26 | D |
| 3 | A | 11 | ABD | 19 | A | 27 | ABD |
| 4 | D | 12 | ABCD | 20 | C | 28 | ACD |
| 5 | B | 13 | ACD | 21 | B | 29 | ABC |
| 6 | C | 14 | ACD | 22 | D | 30 | ABD |
| 7 | A | 15 | ABD | 23 | C |  |  |
| 8 | D | 16 | ABC | 24 | B |  |  |
```

注意：实施时不得保留占位符，场景题关键词表仍只覆盖 `17/18`。

- [ ] **Step 4: 为新增题补齐逐题解析字段**

每道新增题严格补齐：

```markdown
标准答案：

解析：

错项分析：

知识点：

课程映射：

考纲映射：
```

场景题编号保持 `17/18` 不变；新增客观题解析以补充章节方式追加。

- [ ] **Step 5: 运行数量和题号校验**

Run:

```bash
python3 - <<'PY'
import re
from pathlib import Path
path = Path("/Users/admin/openSource/aliyun_acp_learning/exam_materials/C2/模拟题题目.md")
text = path.read_text()
nums = [int(n) for n in re.findall(r"### (\d+)\.", text)]
print("count", len(nums), "first", nums[0], "last", nums[-1], "continuous", nums == list(range(1, nums[-1] + 1)))
PY
```

Expected:

```text
count 30 first 1 last 30 continuous True
```

- [ ] **Step 6: 检查 `C2` 文档诊断**

Run diagnostics on:

```text
file:///Users/admin/openSource/aliyun_acp_learning/exam_materials/C2/模拟题题目.md
file:///Users/admin/openSource/aliyun_acp_learning/exam_materials/C2/模拟题答案解析.md
```

Expected:

```text
无新增诊断错误。
```

---

### Task 3: 扩充 C3 题目与答案解析

**Files:**
- Modify: `exam_materials/C3/模拟题题目.md`
- Modify: `exam_materials/C3/模拟题答案解析.md`

- [ ] **Step 1: 在 `模拟题题目.md` 中追加 4 道单选题**

旧题号不改，单选从 `21` 追加到 `24`，新增题必须覆盖以下至少 4 个不同角度：

```text
1. 工具调用中的参数验证与失败重试
2. 什么时候不该用 Agent 自主规划
3. handoff 与 Leader-Worker 的区别
4. 记忆检索噪声与记忆写入策略
5. Skill 的触发边界与版本演进
6. 评测闭环怎样指导下一轮优化
```

- [ ] **Step 2: 在 `模拟题题目.md` 中追加 2 道多选题**

旧题号不改，多选从 `25` 追加到 `26`，并更新统计区：

```markdown
- 单选题：16
- 多选题：10
- 总题数：26
```

提交答案区改成覆盖 `1-26`：

```markdown
| 1 | ___ | 8 | ___ | 15 | ___ | 22 | ___ |
| 2 | ___ | 9 | ___ | 16 | ___ | 23 | ___ |
| 3 | ___ | 10 | ___ | 17 | ___ | 24 | ___ |
| 4 | ___ | 11 | ___ | 18 | ___ | 25 | ___ |
| 5 | ___ | 12 | ___ | 19 | ___ | 26 | ___ |
| 6 | ___ | 13 | ___ | 20 | ___ |  |  |
| 7 | ___ | 14 | ___ | 21 | ___ |  |  |
```

- [ ] **Step 3: 在 `模拟题答案解析.md` 中更新速查表**

覆盖 `1-26` 全部答案，并确保新增题答案组合不过度集中。新增多选不要继续机械重复 `ABC`。

- [ ] **Step 4: 为新增 6 题补齐完整解析**

每题继续使用固定字段：

```markdown
标准答案：

解析：

错项分析：

知识点：

考纲映射：
```

说明：`C3` 当前解析未使用 `课程映射` 字段，新增题保持与当前 `C3` 文风一致，不强行引入新字段。

- [ ] **Step 5: 运行数量和题号校验**

Run:

```bash
python3 - <<'PY'
import re
from pathlib import Path
path = Path("/Users/admin/openSource/aliyun_acp_learning/exam_materials/C3/模拟题题目.md")
text = path.read_text()
nums = [int(n) for n in re.findall(r"### (\d+)\.", text)]
print("count", len(nums), "first", nums[0], "last", nums[-1], "continuous", nums == list(range(1, nums[-1] + 1)))
PY
```

Expected:

```text
count 26 first 1 last 26 continuous True
```

- [ ] **Step 6: 检查 `C3` 文档诊断**

Run diagnostics on:

```text
file:///Users/admin/openSource/aliyun_acp_learning/exam_materials/C3/模拟题题目.md
file:///Users/admin/openSource/aliyun_acp_learning/exam_materials/C3/模拟题答案解析.md
```

Expected:

```text
无新增诊断错误。
```

---

### Task 4: 修正规格冲突后扩充 C4 题目与答案解析

**Files:**
- Modify: `docs/superpowers/specs/2026-06-23-expand-c2-c3-c4-question-bank-design.md`
- Modify: `exam_materials/C4/模拟题题目.md`
- Modify: `exam_materials/C4/模拟题答案解析.md`

- [ ] **Step 1: 先修正 `C4` 目标题量冲突**

先把规格修正为 `C4` 目标“单选 24 + 多选 14”，并在总量处同步更新；本轮不删除任何旧多选题。

- [ ] **Step 2: 在 `模拟题题目.md` 中追加 6 道单选题**

旧题号不改，单选从 `33` 追加到 `38`，新增题至少覆盖：

```text
1. 蒸馏长尾与数据分布
2. API -> 自部署迁移判断
3. 上下文缓存与批处理边界
4. TTFT、吞吐、成本之间的冲突
5. 护栏、鉴权、审计分层职责
6. 高风险写操作工具的治理
```

- [ ] **Step 3: 在 `模拟题题目.md` 中保留现有 14 道多选题并更新统计**

统计区更新为：

```markdown
- 单选题：24
- 多选题：14
- 总题数：38
```

提交答案区扩成覆盖 `1-38`。

- [ ] **Step 4: 在 `模拟题答案解析.md` 中更新速查表与新增解析**

新增单选 `33-38` 的解析，保留现有多选 `19-32` 的连续结构，速查表同步扩展为：

```text
1-18 旧单选
19-32 旧多选
33-38 新单选
```

每题字段继续保持：

```markdown
标准答案：

解析：

错项分析：

知识点：

考纲映射：
```

- [ ] **Step 5: 运行数量和题号校验**

Run:

```bash
python3 - <<'PY'
import re
from pathlib import Path
path = Path("/Users/admin/openSource/aliyun_acp_learning/exam_materials/C4/模拟题题目.md")
text = path.read_text()
nums = [int(n) for n in re.findall(r"### (\d+)\.", text)]
print("count", len(nums), "first", nums[0], "last", nums[-1], "continuous", nums == list(range(1, nums[-1] + 1)))
PY
```

Expected:

```text
count 38 first 1 last 38 continuous True
```

- [ ] **Step 6: 检查 `C4` 文档诊断**

Run diagnostics on:

```text
file:///Users/admin/openSource/aliyun_acp_learning/exam_materials/C4/模拟题题目.md
file:///Users/admin/openSource/aliyun_acp_learning/exam_materials/C4/模拟题答案解析.md
file:///Users/admin/openSource/aliyun_acp_learning/docs/superpowers/specs/2026-06-23-expand-c2-c3-c4-question-bank-design.md
```

Expected:

```text
无新增诊断错误。
```

---

### Task 5: 全量一致性与重复度复核

**Files:**
- Modify: `exam_materials/C2/模拟题题目.md`
- Modify: `exam_materials/C2/模拟题答案解析.md`
- Modify: `exam_materials/C3/模拟题题目.md`
- Modify: `exam_materials/C3/模拟题答案解析.md`
- Modify: `exam_materials/C4/模拟题题目.md`
- Modify: `exam_materials/C4/模拟题答案解析.md`

- [ ] **Step 1: 做一次题号一致性总检查**

Run:

```bash
python3 - <<'PY'
import re
from pathlib import Path
pairs = [
    ("C2", "/Users/admin/openSource/aliyun_acp_learning/exam_materials/C2/模拟题题目.md", "/Users/admin/openSource/aliyun_acp_learning/exam_materials/C2/模拟题答案解析.md"),
    ("C3", "/Users/admin/openSource/aliyun_acp_learning/exam_materials/C3/模拟题题目.md", "/Users/admin/openSource/aliyun_acp_learning/exam_materials/C3/模拟题答案解析.md"),
    ("C4", "/Users/admin/openSource/aliyun_acp_learning/exam_materials/C4/模拟题题目.md", "/Users/admin/openSource/aliyun_acp_learning/exam_materials/C4/模拟题答案解析.md"),
]
for name, q, a in pairs:
    q_text = Path(q).read_text()
    a_text = Path(a).read_text()
    q_nums = set(map(int, re.findall(r"### (\d+)\.", q_text)))
    a_nums = set(map(int, re.findall(r"### (\d+)\.", a_text)))
    print(name, "question_max", max(q_nums), "answer_has_all", q_nums.issubset(a_nums))
PY
```

Expected:

```text
C2 question_max 24 answer_has_all True
C3 question_max 22 answer_has_all True
C4 question_max 38 answer_has_all True
```

- [ ] **Step 2: 人工复查新增题是否换皮**

逐模块检查新增题，若发现以下情况必须重写：

```text
同一考点只换了场景名
题干变化很小但判断逻辑完全相同
多选题只是把单选题正确项拆成多个选项重复提问
```

- [ ] **Step 3: 人工复查多选答案分布**

检查新增多选题答案组合是否过于机械，至少避免：

```text
新增 4 题里 3 题都是 ABC
新增 2 题全部是 ABCD
新增题所有正确项都固定包含 A
```

- [ ] **Step 4: 运行最终诊断检查**

对 6 个题库文件全部运行 diagnostics，确认无新增格式错误。

- [ ] **Step 5: 准备提交**

Run:

```bash
git status --short
```

Expected:

```text
仅包含本轮规格修正、计划文件和 6 个题库文件的改动。
```

- [ ] **Step 6: 提交**

```bash
git add \
  /Users/admin/openSource/aliyun_acp_learning/docs/superpowers/specs/2026-06-23-expand-c2-c3-c4-question-bank-design.md \
  /Users/admin/openSource/aliyun_acp_learning/docs/superpowers/plans/2026-06-23-expand-c2-c3-c4-question-bank.md \
  /Users/admin/openSource/aliyun_acp_learning/exam_materials/C2/模拟题题目.md \
  /Users/admin/openSource/aliyun_acp_learning/exam_materials/C2/模拟题答案解析.md \
  /Users/admin/openSource/aliyun_acp_learning/exam_materials/C3/模拟题题目.md \
  /Users/admin/openSource/aliyun_acp_learning/exam_materials/C3/模拟题答案解析.md \
  /Users/admin/openSource/aliyun_acp_learning/exam_materials/C4/模拟题题目.md \
  /Users/admin/openSource/aliyun_acp_learning/exam_materials/C4/模拟题答案解析.md
git commit -m "feat: expand c2 c3 c4 question banks"
```

Expected:

```text
[branch-name abc1234] feat: expand c2 c3 c4 question banks
 8 files changed, ...
```
