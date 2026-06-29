# C4 题目质量重做 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 在不改变 `C4` 题号范围和整体结构的前提下，中修重做 `模拟题题目.md` 与 `模拟题答案解析.md`，消除机械多选分布与弱干扰项，提升工程判断区分度。

**Architecture:** 本次只动 `exam_materials/C4/模拟题题目.md` 和 `exam_materials/C4/模拟题答案解析.md`。先固化当前题号边界、目标单选分布与目标多选答案规模，再分两段重写题面，最后同步速查表与逐题解析，并用脚本验证题号、答案覆盖、分布和 diagnostics 是否达标。

**Tech Stack:** Markdown、`python3` 文本校验脚本、VS Code diagnostics、人工题目质量复核

---

### Task 1: 固化 C4 重做边界与目标答案分布

**Files:**
- Modify: `/Users/admin/openSource/aliyun_acp_learning/docs/superpowers/plans/2026-06-23-c4-question-quality-redesign.md`
- Read: `/Users/admin/openSource/aliyun_acp_learning/exam_materials/C4/模拟题题目.md`
- Read: `/Users/admin/openSource/aliyun_acp_learning/exam_materials/C4/模拟题答案解析.md`

- [ ] **Step 1: 记录本轮必须保留的结构边界**

在计划执行日志中先写明以下固定边界，后续任何实现都不能突破：

```text
1. 只修改 C4 的题目与答案解析，不修改考试大纲
2. 保留题号 1-38 不变
3. 保留单选 24、多选 14、总题数 38 不变
4. 保留“提交答案区”和“题型统计”结构
5. 允许重写题干、选项、答案和解析，但不能缩水知识点覆盖
```

- [ ] **Step 2: 固化单选题目标答案分布**

把单选题目标答案表写入本计划，后续重写题目时按此目标落地：

```text
1:B
2:A
3:D
4:C
5:B
6:C
7:A
8:D
9:B
10:A
11:C
12:D
13:B
14:C
15:A
16:D
17:C
18:B
33:A
34:B
35:C
36:D
37:A
38:B
```

说明：

```text
A=6, B=7, C=6, D=5
允许轻微不均匀，但不再出现“明显偏向少数单一字母”
```

- [ ] **Step 3: 固化多选题目标答案规模与组合**

把多选题目标答案表写入本计划，避免继续形成“几乎全是三个正确项”的规律：

```text
19:ABC
20:ACD
21:ABD
22:AB
23:BCD
24:ABCD
25:AC
26:ABD
27:BCD
28:ABC
29:ACD
30:BD
31:ABCD
32:ABCD
```

说明：

```text
1. 允许出现重复组合，但不能由少数组合主导整套多选
2. 必须同时出现 2 项、3 项、4 项答案规模
3. 不能让“默认猜三个答案”继续成为高成功率策略
```

- [ ] **Step 4: 用脚本确认当前题号和分段边界**

Run:

```bash
python3 - <<'PY'
import re
from pathlib import Path
path = Path('/Users/admin/openSource/aliyun_acp_learning/exam_materials/C4/模拟题题目.md')
text = path.read_text()
nums = [int(n) for n in re.findall(r'^###\s+(\d+)\.', text, flags=re.M)]
print('count=', len(nums))
print('first=', nums[0], 'last=', nums[-1])
print('single_range=', nums[:18])
print('multi_range=', nums[18:32])
print('append_single_range=', nums[32:])
PY
```

Expected:

```text
count= 38
first= 1 last= 38
single_range= [1, 2, ..., 18]
multi_range= [19, 20, ..., 32]
append_single_range= [33, 34, 35, 36, 37, 38]
```

- [ ] **Step 5: Commit**

```bash
git add /Users/admin/openSource/aliyun_acp_learning/docs/superpowers/plans/2026-06-23-c4-question-quality-redesign.md
git commit -m "docs: define c4 redesign boundaries and answer distribution"
```

---

### Task 2: 中修重写单选题，消除“概念识别 + 常识排除”

**Files:**
- Modify: `/Users/admin/openSource/aliyun_acp_learning/exam_materials/C4/模拟题题目.md`

- [ ] **Step 1: 重写 `1-18`，保留考点方向但强化工程约束**

按以下主题逐题重写：

```text
1-5: 蒸馏与微调边界 / 数据质量 / 评测指标
6-9: API / 百炼 / vLLM / FC / EAS 等部署选型边界
10-15: 需求分析 / TTFT / 缓存 / 输出约束 / 不默认依赖大模型
16-18: 提示词注入 / 指令注入 / 护栏与权限模型边界
```

每题必须满足：

```text
1. 至少给出一个明确约束：预算、SLO、实时性、运维能力、冷启动、灰度或合规条件
2. 至少 2 个错误项处于同一问题维度
3. 不允许出现“明显离题”或“绝对化口号式”错项
```

- [ ] **Step 2: 重写 `33-38`，把补充单选提升到同一质量标准**

这 6 题分别落在：

```text
33: 蒸馏数据长尾覆盖不足
34: API 到自部署迁移阈值
35: 上下文缓存与公共前缀复用
36: TTFT 优先级判断
37: 护栏 / 鉴权 / 审计职责边界
38: 高风险写操作工具上线治理
```

重写要求：

```text
1. 不再是“看到术语就会”的题
2. 错项必须像真实工程方案，只是错在优先级或上线顺序
3. 题干要体现具体后果、资源条件或治理约束
```

- [ ] **Step 3: 将单选正确答案改成目标分布**

重写完成后，单选答案必须与以下表一致：

```text
1:B 2:A 3:D 4:C 5:B 6:C 7:A 8:D 9:B 10:A 11:C 12:D
13:B 14:C 15:A 16:D 17:C 18:B 33:A 34:B 35:C 36:D 37:A 38:B
```

若某题无法自然落到目标答案，优先继续重写题干与选项，不允许仅为分布好看硬改答案。

- [ ] **Step 4: 用脚本检查单选答案分布**

先手工同步 `模拟题答案解析.md` 中的速查表单选答案，再运行：

```bash
python3 - <<'PY'
from collections import Counter
answers = {
    1:'B',2:'A',3:'D',4:'C',5:'B',6:'C',7:'A',8:'D',9:'B',10:'A',11:'C',12:'D',
    13:'B',14:'C',15:'A',16:'D',17:'C',18:'B',33:'A',34:'B',35:'C',36:'D',37:'A',38:'B'
}
print(Counter(answers.values()))
PY
```

Expected:

```text
Counter({'B': 7, 'A': 6, 'C': 6, 'D': 5})
```

- [ ] **Step 5: Commit**

```bash
git add /Users/admin/openSource/aliyun_acp_learning/exam_materials/C4/模拟题题目.md
git commit -m "docs: rewrite c4 single-choice questions with stronger engineering constraints"
```

---

### Task 3: 中修重写多选题，打散“默认猜三个答案”

**Files:**
- Modify: `/Users/admin/openSource/aliyun_acp_learning/exam_materials/C4/模拟题题目.md`

- [ ] **Step 1: 重写 `19-32`，让多选错项错在边界而不是明显假**

按以下主题逐题重写：

```text
19-21: 蒸馏数据构建 / 过滤 / 适用边界 / 合规前提
22-24: API、自部署、vLLM、FC、EAS、托管平台的取舍
25-27: 需求分析、评测准备、缓存、批量推理、降级与稳定性
28-32: 注入攻击、黑名单边界、护栏能力、风险后果、全链路综合治理
```

重写要求：

```text
1. 每题至少 3 个选项看起来都像可行方案
2. 错项要错在约束不满足、治理不完整、优先级错误或过度绝对化
3. 不允许继续出现“读主题就默认猜三个答案”的题
```

- [ ] **Step 2: 将多选答案改成目标组合**

多选题答案必须落到以下组合：

```text
19:ABC
20:ACD
21:ABD
22:AB
23:BCD
24:ABCD
25:AC
26:ABD
27:BCD
28:ABC
29:ACD
30:BD
31:ABCD
32:ABCD
```

- [ ] **Step 3: 人工复查多选正确项是否由题面逻辑驱动**

逐题确认以下四点：

```text
1. 正确项不是为了打散分布而硬凑出来的
2. 错误项至少有一个“局部正确但整体不成立”
3. 不存在“只因表达更全面就显得正确”的选项
4. 2 项 / 3 项 / 4 项答案规模都由题面逻辑驱动，而不是纯形式打散
```

- [ ] **Step 4: 用脚本检查多选答案规模与组合分布**

Run:

```bash
python3 - <<'PY'
from collections import Counter
answers = {
    19:'ABC',20:'ACD',21:'ABD',22:'AB',23:'BCD',24:'ABCD',25:'AC',
    26:'ABD',27:'BCD',28:'ABC',29:'ACD',30:'BD',31:'ABCD',32:'ABCD'
}
print('combo=', Counter(answers.values()))
print('size=', Counter(len(v) for v in answers.values()))
PY
```

Expected:

```text
combo= Counter({'ABCD': 3, 'ABC': 2, 'ACD': 2, 'ABD': 2, 'BCD': 2, 'AB': 1, 'AC': 1, 'BD': 1})
size= Counter({3: 8, 4: 3, 2: 3})
```

并人工确认：已出现 `2` 项、`3` 项、`4` 项三种答案规模。

- [ ] **Step 5: Commit**

```bash
git add /Users/admin/openSource/aliyun_acp_learning/exam_materials/C4/模拟题题目.md
git commit -m "docs: rewrite c4 multiple-choice questions and diversify answer sizes"
```

---

### Task 4: 同步重写答案解析与速查表

**Files:**
- Modify: `/Users/admin/openSource/aliyun_acp_learning/exam_materials/C4/模拟题答案解析.md`

- [ ] **Step 1: 重写速查表，覆盖 `1-38` 新答案**

将速查表更新为与新题完全同步，至少满足以下答案：

```md
| 1 | B | 11 | C | 21 | ABD | 31 | ABCD |
| 2 | A | 12 | D | 22 | AB | 32 | ABCD |
| 3 | D | 13 | B | 23 | BCD | 33 | A |
| 4 | C | 14 | C | 24 | ABCD | 34 | B |
| 5 | B | 15 | A | 25 | AC | 35 | C |
| 6 | C | 16 | D | 26 | ABD | 36 | D |
| 7 | A | 17 | C | 27 | BCD | 37 | A |
| 8 | D | 18 | B | 28 | ABC | 38 | B |
| 9 | B | 19 | ABC | 29 | ACD |  |  |
| 10 | A | 20 | ACD | 30 | BD |  |  |
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
4. 重点题要写出为什么“更强方案”不一定在当前约束下更优
```

- [ ] **Step 3: 更新文末复习建议，反映本轮重做重点**

将结尾调整为覆盖以下四点：

```text
1. 蒸馏适用边界、数据质量与长尾覆盖
2. API / 自部署 / vLLM / FC / EAS 的选型边界
3. 生产环境里的 SLO、TTFT、缓存、降级与模板化链路
4. 注入攻击、护栏、鉴权、审计与高风险写工具治理
```

- [ ] **Step 4: 用脚本验证题号与解析覆盖一致**

Run:

```bash
python3 - <<'PY'
import re
from pathlib import Path
q = Path('/Users/admin/openSource/aliyun_acp_learning/exam_materials/C4/模拟题题目.md').read_text()
a = Path('/Users/admin/openSource/aliyun_acp_learning/exam_materials/C4/模拟题答案解析.md').read_text()
q_nums = [int(x) for x in re.findall(r'^###\s+(\d+)\.', q, flags=re.M)]
a_nums = sorted(set(int(x) for x in re.findall(r'^###\s+(\d+)\.', a, flags=re.M)))
print('question_count=', len(q_nums))
print('answer_has_all=', set(q_nums).issubset(set(a_nums)))
print('question_last=', q_nums[-1], 'answer_last=', max(a_nums))
PY
```

Expected:

```text
question_count= 38
answer_has_all= True
question_last= 38 answer_last= 38
```

- [ ] **Step 5: Commit**

```bash
git add /Users/admin/openSource/aliyun_acp_learning/exam_materials/C4/模拟题答案解析.md
git commit -m "docs: sync c4 answer analysis with redesigned question set"
```

---

### Task 5: 最终一致性验收与文档诊断

**Files:**
- Modify: `/Users/admin/openSource/aliyun_acp_learning/exam_materials/C4/模拟题题目.md`
- Modify: `/Users/admin/openSource/aliyun_acp_learning/exam_materials/C4/模拟题答案解析.md`

- [ ] **Step 1: 复查“弱干扰项”是否仍明显存在**

人工逐题检查以下失败模式：

```text
1. 有两个以上选项明显离题
2. 正确项因“最完整、最先进、最像标准答案”而过于突出
3. 错误项并非同维度竞争
4. 仅凭常识即可在不理解 C4 工程边界的情况下做对
5. 多选题仍能通过“默认猜三个答案”取得高命中率
```

- [ ] **Step 2: 复查答案分布是否达标**

Run:

```bash
python3 - <<'PY'
from collections import Counter
single = ['B','A','D','C','B','C','A','D','B','A','C','D','B','C','A','D','C','B','A','B','C','D','A','B']
multi = ['ABC','ACD','ABD','AB','BCD','ABCD','AC','ABD','BCD','ABC','ACD','BD','ABCD','ABCD']
print('single=', Counter(single))
print('multi_combo=', Counter(multi))
print('multi_size=', Counter(len(x) for x in multi))
PY
```

Expected:

```text
single= Counter({'B': 7, 'A': 6, 'C': 6, 'D': 5})
multi_combo= Counter({'ABCD': 3, 'ABC': 2, 'ACD': 2, 'ABD': 2, 'BCD': 2, 'AB': 1, 'AC': 1, 'BD': 1})
multi_size= Counter({3: 8, 4: 3, 2: 3})
```

- [ ] **Step 3: 运行 diagnostics**

对以下文件运行 diagnostics：

```text
file:///Users/admin/openSource/aliyun_acp_learning/exam_materials/C4/模拟题题目.md
file:///Users/admin/openSource/aliyun_acp_learning/exam_materials/C4/模拟题答案解析.md
file:///Users/admin/openSource/aliyun_acp_learning/docs/superpowers/specs/2026-06-23-c4-question-quality-redesign-design.md
file:///Users/admin/openSource/aliyun_acp_learning/docs/superpowers/plans/2026-06-23-c4-question-quality-redesign.md
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
1. docs/superpowers/specs/2026-06-23-c4-question-quality-redesign-design.md
2. docs/superpowers/plans/2026-06-23-c4-question-quality-redesign.md
3. exam_materials/C4/模拟题题目.md
4. exam_materials/C4/模拟题答案解析.md
```

- [ ] **Step 5: Commit**

```bash
git add \
  /Users/admin/openSource/aliyun_acp_learning/docs/superpowers/specs/2026-06-23-c4-question-quality-redesign-design.md \
  /Users/admin/openSource/aliyun_acp_learning/docs/superpowers/plans/2026-06-23-c4-question-quality-redesign.md \
  /Users/admin/openSource/aliyun_acp_learning/exam_materials/C4/模拟题题目.md \
  /Users/admin/openSource/aliyun_acp_learning/exam_materials/C4/模拟题答案解析.md
git commit -m "docs: redesign c4 question quality and answer distribution"
```
