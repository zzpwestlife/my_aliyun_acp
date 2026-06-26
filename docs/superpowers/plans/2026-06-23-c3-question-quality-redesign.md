# C3 题目质量重做 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 在不改变 `C3` 题号范围和整体结构的前提下，中修重做 `模拟题题目.md` 与 `模拟题答案解析.md`，消除弱干扰项与机械答案分布。

**Architecture:** 本次只动 `exam_materials/C3/模拟题题目.md` 和 `exam_materials/C3/模拟题答案解析.md`。先盘点当前单选/多选的泄题模式和目标答案分布，再分两段重写题面，最后同步速查表与逐题解析，并用脚本验证题号、答案覆盖和分布是否达标。

**Tech Stack:** Markdown、`python3` 文本校验脚本、VS Code diagnostics、人工题目质量复核

---

### Task 1: 固化 C3 重做边界与目标答案分布

**Files:**
- Modify: `/Users/admin/openSource/aliyun_acp_learning/docs/superpowers/plans/2026-06-23-c3-question-quality-redesign.md`
- Read: `/Users/admin/openSource/aliyun_acp_learning/exam_materials/C3/模拟题题目.md`
- Read: `/Users/admin/openSource/aliyun_acp_learning/exam_materials/C3/模拟题答案解析.md`

- [ ] **Step 1: 记录本轮必须保留的结构边界**

在计划执行日志中先写明以下固定边界，后续任何实现都不能突破：

```text
1. 只修改 C3 的题目与答案解析，不修改考试大纲
2. 保留题号 1-26 不变
3. 保留单选 16、多选 10、总题数 26 不变
4. 保留“提交答案区”和“题型统计”结构
5. 允许重写题干、选项、答案和解析，但不能缩水知识点覆盖
```

- [ ] **Step 2: 固化单选题目标答案分布**

把单选题目标答案表写入本计划，后续重写题目时按此目标落地：

```text
1:B
2:A
3:C
4:B
5:D
6:A
7:C
8:B
9:D
10:A
11:C
12:B
21:D
22:B
23:A
24:C
```

说明：

```text
A=4, B=5, C=4, D=3
允许轻微不均匀，但不再出现“绝大多数都是 B”
```

- [ ] **Step 3: 固化多选题目标答案分布**

把多选题目标答案表写入本计划，避免再次大面积集中在 `ABC`：

```text
13:ABC
14:ACD
15:ABD
16:ABC
17:BCD
18:ABD
19:ABC
20:ACD
25:ACD
26:ABC
```

说明：

```text
1. 允许出现重复组合，但不能形成“几乎清一色 ABC”
2. 至少要出现 ABC / ABD / ACD / BCD 四种组合
```

- [ ] **Step 4: 用脚本确认当前题号和分段边界**

Run:

```bash
python3 - <<'PY'
import re
from pathlib import Path
path = Path('/Users/admin/openSource/aliyun_acp_learning/exam_materials/C3/模拟题题目.md')
text = path.read_text()
nums = [int(n) for n in re.findall(r'^###\s+(\d+)\.', text, flags=re.M)]
print('count=', len(nums))
print('first=', nums[0], 'last=', nums[-1])
print('single_range=', nums[:12])
print('multi_range=', nums[12:20])
print('append_single_range=', nums[20:24])
print('append_multi_range=', nums[24:])
PY
```

Expected:

```text
count= 26
first= 1 last= 26
single_range= [1, 2, ..., 12]
multi_range= [13, 14, ..., 20]
append_single_range= [21, 22, 23, 24]
append_multi_range= [25, 26]
```

- [ ] **Step 5: Commit**

```bash
git add /Users/admin/openSource/aliyun_acp_learning/docs/superpowers/plans/2026-06-23-c3-question-quality-redesign.md
git commit -m "docs: define c3 redesign boundaries and answer distribution"
```

---

### Task 2: 中修重写单选题，消除“全是 B”和常识秒杀

**Files:**
- Modify: `/Users/admin/openSource/aliyun_acp_learning/exam_materials/C3/模拟题题目.md`

- [ ] **Step 1: 重写 `1-12`，保留考点方向但强化约束条件**

按以下规则逐题重写：

```text
1-3: 工具调用与协议边界
4-5: 工作流 / 规划 / 反馈
6-7: 多 Agent 协作模式
8-9: 短期 / 长期记忆边界
10: Skill 沉淀
11: 白盒评测
12: 综合能力组合
```

每题必须满足：

```text
1. 至少给出一个明确约束：实时性、可控性、失败成本、上下文长度、是否有总控等
2. 至少 2 个错误项必须处于同一问题维度
3. 不允许出现“完全离题”的凑数选项
```

- [ ] **Step 2: 重写 `21-24`，把补充单选提升到同一质量标准**

这 4 题分别落在：

```text
21: 写操作工具幂等与重试治理
22: 何时不该用自主规划
23: handoff 与 Leader-Worker 边界
24: 长期记忆写入与噪声控制
```

重写要求：

```text
1. 不再是“只看术语就会”的题
2. 错项必须看起来像真实工程方案，只是错在边界
3. 题干要体现具体后果或系统约束
```

- [ ] **Step 3: 将单选正确答案改成目标分布**

重写完成后，单选答案必须与以下表一致：

```text
1:B 2:A 3:C 4:B 5:D 6:A 7:C 8:B
9:D 10:A 11:C 12:B 21:D 22:B 23:A 24:C
```

若某题无法自然落到目标答案，优先继续重写题干与选项，不允许仅为分布好看硬改答案。

- [ ] **Step 4: 用脚本检查单选答案分布**

先手工同步 `模拟题答案解析.md` 中的速查表单选答案，再运行：

```bash
python3 - <<'PY'
from collections import Counter
answers = {
    1:'B',2:'A',3:'C',4:'B',5:'D',6:'A',7:'C',8:'B',
    9:'D',10:'A',11:'C',12:'B',21:'D',22:'B',23:'A',24:'C'
}
print(Counter(answers.values()))
PY
```

Expected:

```text
Counter({'B': 5, 'A': 4, 'C': 4, 'D': 3})
```

- [ ] **Step 5: Commit**

```bash
git add /Users/admin/openSource/aliyun_acp_learning/exam_materials/C3/模拟题题目.md
git commit -m "docs: rewrite c3 single-choice questions with stronger distractors"
```

---

### Task 3: 中修重写多选题，打散机械 `ABC`

**Files:**
- Modify: `/Users/admin/openSource/aliyun_acp_learning/exam_materials/C3/模拟题题目.md`

- [ ] **Step 1: 重写 `13-20`，让错项错在边界而不是明显假**

按以下主题逐题重写：

```text
13: 工具调用可靠性
14: 固定工作流 / Plan & Execute / 外部反馈
15: Leader-Worker / Blackboard / handoff
16: 截断 / 摘要 / 向量召回 / 长期写入
17: Skill 触发边界与版本化
18: 白盒 / 端到端 / 持续评测
19: Qwen Code 方法边界
20: 工具 + Skill + 记忆 + 评测闭环
25: Skill 的产品化与依赖定义
26: 评测结果如何反哺下一轮优化
```

重写要求：

```text
1. 每题至少 3 个选项看起来都像可行方案
2. 错项要错在过度泛化、缺失前提或忽略代价
3. 不允许继续出现“读主题就直接猜 ABC”的题
```

- [ ] **Step 2: 将多选答案改成目标组合**

多选题答案必须落到以下组合：

```text
13:ABC
14:ACD
15:ABD
16:ABC
17:BCD
18:ABD
19:ABC
20:ACD
25:ACD
26:ABC
```

- [ ] **Step 3: 人工复查多选正确项是否由题面逻辑驱动**

逐题确认以下三点：

```text
1. 正确项不是为了打散分布而硬凑出来的
2. 错误项至少有一个“局部正确但整体不成立”
3. 不存在“只因表达更全面就显得正确”的选项
```

- [ ] **Step 4: 用脚本检查多选答案组合分布**

Run:

```bash
python3 - <<'PY'
from collections import Counter
answers = {
    13:'ABC',14:'ACD',15:'ABD',16:'ABC',17:'BCD',
    18:'ABD',19:'ABC',20:'ACD',25:'ACD',26:'ABC'
}
print(Counter(answers.values()))
PY
```

Expected:

```text
Counter({'ABC': 4, 'ACD': 3, 'ABD': 2, 'BCD': 1})
```

并人工确认：已出现 `ABC / ABD / ACD / BCD` 四种组合。

- [ ] **Step 5: Commit**

```bash
git add /Users/admin/openSource/aliyun_acp_learning/exam_materials/C3/模拟题题目.md
git commit -m "docs: rewrite c3 multiple-choice questions and diversify answer patterns"
```

---

### Task 4: 同步重写答案解析与速查表

**Files:**
- Modify: `/Users/admin/openSource/aliyun_acp_learning/exam_materials/C3/模拟题答案解析.md`

- [ ] **Step 1: 重写速查表，覆盖 `1-26` 新答案**

将速查表更新为与新题完全同步，至少满足以下答案：

```md
| 1 | B | 8 | B | 15 | ABD | 22 | B |
| 2 | A | 9 | D | 16 | ABC | 23 | A |
| 3 | C | 10 | A | 17 | BCD | 24 | C |
| 4 | B | 11 | C | 18 | ABD | 25 | ACD |
| 5 | D | 12 | B | 19 | ABC | 26 | ABC |
| 6 | A | 13 | ABC | 20 | ACD |  |  |
| 7 | C | 14 | ACD | 21 | D |  |  |
```

- [ ] **Step 2: 对所有被重写题面同步改写解析**

每道题继续使用当前字段：

```md
标准答案：

解析：

错项分析：

知识点：

考纲映射：
```

具体要求：

```text
1. 单选题至少解释 1 个最具迷惑性的错项
2. 多选题要解释为什么某个“看起来合理”的项不能入选
3. 被改成新答案的题，解析必须完整更新，不能保留旧逻辑
```

- [ ] **Step 3: 更新文末复习建议，反映本轮重做重点**

将结尾调整为覆盖以下四点：

```text
1. 工具调用边界与写操作治理
2. 工作流 / 自主规划 / 反馈机制边界
3. 协作模式与记忆治理
4. Skill 与评测闭环的工程组合
```

- [ ] **Step 4: 用脚本验证题号与解析覆盖一致**

Run:

```bash
python3 - <<'PY'
import re
from pathlib import Path
q = Path('/Users/admin/openSource/aliyun_acp_learning/exam_materials/C3/模拟题题目.md').read_text()
a = Path('/Users/admin/openSource/aliyun_acp_learning/exam_materials/C3/模拟题答案解析.md').read_text()
q_nums = [int(x) for x in re.findall(r'^###\s+(\d+)\.', q, flags=re.M)]
a_nums = sorted(set(int(x) for x in re.findall(r'^###\s+(\d+)\.', a, flags=re.M)))
print('question_count=', len(q_nums))
print('answer_has_all=', set(q_nums).issubset(set(a_nums)))
print('question_last=', q_nums[-1], 'answer_last=', max(a_nums))
PY
```

Expected:

```text
question_count= 26
answer_has_all= True
question_last= 26 answer_last= 26
```

- [ ] **Step 5: Commit**

```bash
git add /Users/admin/openSource/aliyun_acp_learning/exam_materials/C3/模拟题答案解析.md
git commit -m "docs: sync c3 answer analysis with redesigned question set"
```

---

### Task 5: 最终一致性验收与文档诊断

**Files:**
- Modify: `/Users/admin/openSource/aliyun_acp_learning/exam_materials/C3/模拟题题目.md`
- Modify: `/Users/admin/openSource/aliyun_acp_learning/exam_materials/C3/模拟题答案解析.md`

- [ ] **Step 1: 复查“弱干扰项”是否仍明显存在**

人工逐题检查以下失败模式：

```text
1. 有两个以上选项明显离题
2. 正确项因“最完整、最先进、最像标准答案”而过于突出
3. 错误项并非同维度竞争
4. 仅凭常识就能在不理解 C3 边界的情况下做对
```

- [ ] **Step 2: 复查答案分布是否达标**

Run:

```bash
python3 - <<'PY'
from collections import Counter
single = ['B','A','C','B','D','A','C','B','D','A','C','B','D','B','A','C']
multi = ['ABC','ACD','ABD','ABC','BCD','ABD','ABC','ACD','ACD','ABC']
print('single=', Counter(single))
print('multi=', Counter(multi))
PY
```

Expected:

```text
single= Counter({'B': 5, 'A': 4, 'C': 4, 'D': 3})
multi= Counter({'ABC': 4, 'ACD': 3, 'ABD': 2, 'BCD': 1})
```

- [ ] **Step 3: 运行 diagnostics**

对以下文件运行 diagnostics：

```text
file:///Users/admin/openSource/aliyun_acp_learning/exam_materials/C3/模拟题题目.md
file:///Users/admin/openSource/aliyun_acp_learning/exam_materials/C3/模拟题答案解析.md
file:///Users/admin/openSource/aliyun_acp_learning/docs/superpowers/specs/2026-06-23-c3-question-quality-redesign-design.md
file:///Users/admin/openSource/aliyun_acp_learning/docs/superpowers/plans/2026-06-23-c3-question-quality-redesign.md
```

Expected:

```text
无新增诊断错误。
```

- [ ] **Step 4: 检查工作区变更范围**

Run:

```bash
git status --short
```

Expected:

```text
本轮新增或修改的重点文件应为：
1. docs/superpowers/specs/2026-06-23-c3-question-quality-redesign-design.md
2. docs/superpowers/plans/2026-06-23-c3-question-quality-redesign.md
3. exam_materials/C3/模拟题题目.md
4. exam_materials/C3/模拟题答案解析.md
```

- [ ] **Step 5: Commit**

```bash
git add \
  /Users/admin/openSource/aliyun_acp_learning/docs/superpowers/specs/2026-06-23-c3-question-quality-redesign-design.md \
  /Users/admin/openSource/aliyun_acp_learning/docs/superpowers/plans/2026-06-23-c3-question-quality-redesign.md \
  /Users/admin/openSource/aliyun_acp_learning/exam_materials/C3/模拟题题目.md \
  /Users/admin/openSource/aliyun_acp_learning/exam_materials/C3/模拟题答案解析.md
git commit -m "docs: redesign c3 question quality and answer distribution"
```
