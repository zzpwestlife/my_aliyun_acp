# C4 题目质量升级 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将 `exam_materials/C4` 升级为一套高质量“交付上线”模块题库，让 `考试大纲.md`、`模拟题题目.md`、`模拟题答案解析.md` 在命题分层、工程判断感和解析复盘质量上完全对齐。

**Architecture:** 先把 `考试大纲.md` 改造成命题基线稿，明确 `4.1` 到 `4.4` 各模块的考核层级、建议难度、命题方式和易错方向；再重写 `模拟题题目.md`，保留 `32` 题规模，但重构为更强的工程判断题、方案选型题和系统边界题；最后同步升级 `模拟题答案解析.md`，为每题补齐标准答案、解析、错项分析、知识点与考纲映射，并做全卷一致性校验。

**Tech Stack:** Markdown，现有 `exam_materials/C4` 材料，`python3` 文本校验脚本，人工题目质量复核

---

### Task 1: 重构 C4 考试大纲，建立交付上线模块命题基线

**Files:**
- Modify: `/Users/admin/openSource/aliyun_acp_learning/exam_materials/C4/考试大纲.md`

- [ ] **Step 1: 重写文档头部，明确 C4 的命题定位**

将文档开头替换为以下结构：

```md
# C4 考试大纲

本文档用于支撑 `C4` 模块题库升级，不仅整理《阿里云大模型 ACP 考试大纲》中与“交付上线”相关的核心要求，也明确每类考点适合出的题型和难度层级，作为 `模拟题题目.md` 与 `模拟题答案解析.md` 的命题基线。

## 一、模块定位与权重

- 模块名称：`C4 交付上线`
- 对应教程：`4_0` 到 `4_4`
- 对应考试大纲板块：模型定制与优化、生产环境应用实践、安全与合规
- 模块特征：更强调工程判断、方案选型、上线治理和纵深防御
```

- [ ] **Step 2: 将正文改造成“模块 -> 考点 -> 考核层级 -> 建议难度 -> 常见命题方式”矩阵**

正文必须覆盖以下模块，并统一使用这个表头：

```md
| 模块 | 考点 | 考核层级 | 建议难度 | 常见命题方式 |
| --- | --- | --- | --- | --- |
| 蒸馏与微调边界 | 任务适配性、数据构建、评测指标、合规边界 | 掌握 / 应用 | 基础 / 中档 / 拔高 | 任务选型、过滤优先级、评测优先级 |
| 模型部署与发布选型 | API、百炼、vLLM、PAI-EAS、FC、ACK、ECS | 理解 / 应用 | 基础 / 中档 / 拔高 | 方案选型、阶段性迁移、性能边界 |
| 生产环境应用实践 | 功能性需求、非功能性需求、TTFT、缓存、降级、稳定性 | 掌握 / 应用 | 基础 / 中档 / 拔高 | 需求优先级、SLO、体验与稳定性判断 |
| 安全合规与纵深防御 | 提示词注入、工具风险、黑名单、AI 护栏、权限模型 | 理解 / 应用 | 中档 / 拔高 | 攻击识别、职责边界、纵深防御设计 |
```

- [ ] **Step 3: 新增“命题难度分布建议”和“易错方向”**

在文末加入：

```md
## 三、命题难度分布建议

- 单选题 `18`：基础 `7`、中档 `8`、拔高 `3`
- 多选题 `14`：基础 `5`、中档 `6`、拔高 `3`

## 四、易错方向

- 把“适合蒸馏”和“适合 RAG / 在线大模型”混为一谈。
- 把“能起服务”和“能承接生产流量”混为一谈。
- 只记性能指标名称，不会判断需求优先级和生产治理顺序。
- 把 AI 护栏误当成权限模型和工具鉴权的替代品。
```

- [ ] **Step 4: 用脚本检查大纲是否包含关键字段和模块**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
text = Path('/Users/admin/openSource/aliyun_acp_learning/exam_materials/C4/考试大纲.md').read_text()
for key in ['考核层级', '建议难度', '常见命题方式', '命题难度分布建议', '易错方向', 'AI 护栏']:
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
AI 护栏 True
```

- [ ] **Step 5: Commit**

```bash
git add /Users/admin/openSource/aliyun_acp_learning/exam_materials/C4/考试大纲.md
git commit -m "docs: rebuild c4 outline as production exam authoring baseline"
```

### Task 2: 重写 C4 模拟题题目，保留 32 题并提升工程判断感

**Files:**
- Modify: `/Users/admin/openSource/aliyun_acp_learning/exam_materials/C4/模拟题题目.md`

- [ ] **Step 1: 重写考试说明，锁定 32 题与难度梯度**

将文档头部改成：

```md
# C4 模拟题题目

## 考试说明

- 本卷为 `C4` 质量升级试点卷，共 `32` 题。
- 单选题 `18` 题，多选题 `14` 题。
- 难度结构：基础题 `12`、中档题 `14`、拔高题 `6`。
- 建议时长：`70` 到 `75` 分钟。
- 建议先独立作答，再对照 `模拟题答案解析.md` 复盘。
```

- [ ] **Step 2: 重写 18 道单选题，确保四大模块覆盖清晰**

单选题按以下主题重写：

```text
1-5: 4.1 蒸馏与微调边界
6-9: 4.2 部署与发布选型
10-15: 4.3 生产环境应用实践
16-18: 4.4 安全合规与综合
```

每题采用如下格式：

```md
### 1. 【中档·4.1】题干……

- A. …
- B. …
- C. …
- D. …
```

并满足：

```text
1. 至少 10 道单选题带明确场景前提
2. 至少 8 道单选题体现方案选型、优先级或系统边界判断
3. 拔高题必须体现跨模块工程完整性
```

- [ ] **Step 3: 重写 14 道多选题，控制答案组合和综合题质量**

多选题按以下主题设计：

```text
19-21: 4.1 蒸馏数据、评测、适配边界
22-24: 4.2 API / vLLM / 云上部署取舍
25-27: 4.3 需求分析、性能优化、稳定性设计
28-31: 4.4 注入攻击、黑名单、AI 护栏、风险后果
32: 4.1-4.4 综合能力组合
```

要求：

```text
1. 多选题答案组合不得大量重复 ABCD
2. 至少 8 道多选题含条件或限制前提
3. 综合题要考“完整工程链路”，不能只是概念并列
```

- [ ] **Step 4: 调整作答建议和题型统计**

将文末更新为：

```md
## 题型统计

- 单选题：18
- 多选题：14
- 总题数：32
```

作答建议需围绕蒸馏边界、部署选型、生产治理和纵深防御四个维度判断。

- [ ] **Step 5: 用脚本检查题号和总题量**

Run:

```bash
python3 - <<'PY'
import re
from pathlib import Path
text = Path('/Users/admin/openSource/aliyun_acp_learning/exam_materials/C4/模拟题题目.md').read_text()
nums = re.findall(r'^###\\s+(\\d+)\\.', text, flags=re.M)
print('count=', len(nums))
print('first=', nums[0], 'last=', nums[-1])
print('unique=', len(set(nums)) == len(nums))
PY
```

Expected:

```text
count= 32
first= 1 last= 32
unique= True
```

- [ ] **Step 6: Commit**

```bash
git add /Users/admin/openSource/aliyun_acp_learning/exam_materials/C4/模拟题题目.md
git commit -m "docs: rebuild c4 objective exam with stronger production judgment"
```

### Task 3: 重写 C4 模拟题答案解析，建立高质量复盘链路

**Files:**
- Modify: `/Users/admin/openSource/aliyun_acp_learning/exam_materials/C4/模拟题答案解析.md`

- [ ] **Step 1: 重写速查表，保持与 32 题新试卷完全同步**

文档头部统一为：

```md
# C4 模拟题答案解析

## 使用说明
- 配合 `模拟题题目.md` 使用。
- 建议先完整作答，再结合速查表和逐题解析复盘。
- 中档题和拔高题优先看“错项分析”和“工程判断依据”。

## 标准答案速查表
```

速查表要求：

```text
1. 覆盖 1 至 32 题
2. 单选与多选分布清晰
3. 不能保留旧题答案组合
```

- [ ] **Step 2: 为 1 至 32 题统一补齐解析字段**

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
2. 中档题必须解释为什么这个选型或边界更合理
3. 拔高题必须指出为什么该方案更完整、其他方案只是局部正确
```

- [ ] **Step 3: 重写文末“考点覆盖与复习建议”**

将结尾改成：

```md
## 考点覆盖与复习建议

- 先复习 `4.1` 蒸馏边界与数据质量，再看 `4.2` 的部署选型。
- 再复习 `4.3` 的需求分析、SLO、稳定性和降本路径。
- 最后复习 `4.4` 的注入攻击、护栏、权限模型与纵深防御，并把四部分串成完整上线链路。
```

- [ ] **Step 4: 用脚本校验解析题号与题面一致**

Run:

```bash
python3 - <<'PY'
import re
from pathlib import Path
q = Path('/Users/admin/openSource/aliyun_acp_learning/exam_materials/C4/模拟题题目.md').read_text()
a = Path('/Users/admin/openSource/aliyun_acp_learning/exam_materials/C4/模拟题答案解析.md').read_text()
q_nums = re.findall(r'^###\\s+(\\d+)\\.', q, flags=re.M)
a_nums = re.findall(r'^###\\s+(\\d+)\\.', a, flags=re.M)
print('question_count=', len(q_nums))
print('answer_count=', len(a_nums))
print('same=', q_nums == a_nums)
PY
```

Expected:

```text
question_count= 32
answer_count= 32
same= True
```

- [ ] **Step 5: Commit**

```bash
git add /Users/admin/openSource/aliyun_acp_learning/exam_materials/C4/模拟题答案解析.md
git commit -m "docs: rebuild c4 answer key with rationale and mapping"
```

### Task 4: 做 C4 整套一致性验收，确认可作为交付上线模块样板

**Files:**
- Modify: `/Users/admin/openSource/aliyun_acp_learning/exam_materials/C4/考试大纲.md`
- Modify: `/Users/admin/openSource/aliyun_acp_learning/exam_materials/C4/模拟题题目.md`
- Modify: `/Users/admin/openSource/aliyun_acp_learning/exam_materials/C4/模拟题答案解析.md`

- [ ] **Step 1: 检查核心考点是否均已落题**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
outline = Path('/Users/admin/openSource/aliyun_acp_learning/exam_materials/C4/考试大纲.md').read_text()
questions = Path('/Users/admin/openSource/aliyun_acp_learning/exam_materials/C4/模拟题题目.md').read_text()
for key in ['蒸馏', 'vLLM', '函数计算', 'TTFT', 'AI 护栏', '权限模型']:
    print(f'{key}: outline={key in outline}, questions={key in questions}')
PY
```

Expected: 关键主题在大纲和题面中都能找到落点。

- [ ] **Step 2: 检查难度梯度与题型分布**

人工核对：

```text
1. 基础题约 12 道
2. 中档题约 14 道
3. 拔高题约 6 道
4. 单选 18 道
5. 多选 14 道
```

- [ ] **Step 3: 检查解析字段完整性**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
text = Path('/Users/admin/openSource/aliyun_acp_learning/exam_materials/C4/模拟题答案解析.md').read_text()
for key in ['标准答案：', '解析：', '错项分析：', '知识点：', '考纲映射：']:
    print(key, text.count(key))
PY
```

Expected: 每个字段都出现多次，足以覆盖全部 32 题。

- [ ] **Step 4: 最终人工验收清单**

逐项核对：

```text
1. 是否仍保留偏知识点摘抄的题目
2. 是否仍有明显一眼排除的弱干扰项
3. 是否存在多选题答案组合重复过多
4. 是否有解析缺少错项分析
5. 是否有 4.1-4.4 的核心模块未在题目中体现
```

- [ ] **Step 5: Commit**

```bash
git add /Users/admin/openSource/aliyun_acp_learning/exam_materials/C4/考试大纲.md /Users/admin/openSource/aliyun_acp_learning/exam_materials/C4/模拟题题目.md /Users/admin/openSource/aliyun_acp_learning/exam_materials/C4/模拟题答案解析.md
git commit -m "docs: finalize c4 as high-quality production exam pack pilot"
```
