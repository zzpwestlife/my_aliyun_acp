# RAG 优化方法对比表 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 新增一份以 ACP 考纲优先视角编写的 RAG 优化方法对比文档，帮助区分句子窗口检索、自动合并检索、重排序和标题改写。

**Architecture:** 本次只新增一个 Markdown 复习文档，不改现有题库。文档采用“说明 + 横向对比表 + 结论 + 速记提示”的固定结构，明确区分考纲视角与课内是否出现。

**Tech Stack:** Markdown、现有仓库课件与题库口径

---

### Task 1: 生成 RAG 优化方法对比文档

**Files:**
- Create: `.trae/specs/generate-c2-mock-exam/rag-optimization-comparison.md`
- Reference: `docs/superpowers/specs/2026-06-11-rag-optimization-comparison-design.md`

- [ ] **Step 1: 写入标题与说明区**

创建文件并写入开头说明，包含以下内容：

```md
# RAG 优化方法对比表

> 口径说明：本文采用“ACP 考纲优先”视角整理，适合考试复习；其中部分术语可能属于考纲扩展理解，不一定在当前 C2 课内材料中以同名原词出现。
```

- [ ] **Step 2: 写入核心对比表**

在文档中加入 Markdown 表格，至少包含以下列：

```md
| 概念 | 一句话定义 | 主要解决的问题 | 所处阶段 | 对 RAG 的主要作用 | 课内是否明确出现 | ACP 复习建议 |
| --- | --- | --- | --- | --- | --- | --- |
```

并覆盖以下 4 行：

```md
| 句子窗口检索 | 命中某个片段后，同时补回其附近句子或上下文窗口 | 只命中单句、上下文不完整 | 检索后上下文扩展 | 让召回内容更完整 | 是 | 记成“命中后补邻近上下文” |
| 自动合并检索 | 命中多个相邻小块后，自动合并成更完整的段落或章节片段 | 文本切块过碎、语义被拆散 | 检索后结果合并 | 把碎片拼回较完整语义单元 | 否 | 记成“把碎片自动拼起来” |
| 重排序 | 对初步召回的候选结果再做相关性排序 | 初召回有噪声，最相关内容没排前面 | 检索后排序优化 | 让更相关的片段排在前面 | 是 | 记成“召回后再排一次序” |
| 标题改写 | 给文档片段补充更利于检索的标题或结构化描述 | 原始片段语义弱、检索信号不足 | 索引构建/切片增强 | 让块本身更容易被召回 | 是 | 记成“先把块写得更好找” |
```

- [ ] **Step 3: 写入结论区**

在表格后加入以下 3 段结论：

```md
## 结论

### 1. 从技术作用上区分

- 句子窗口检索：重点是“补周边上下文”。
- 自动合并检索：重点是“把多个碎块拼成完整语义单元”。
- 重排序：重点是“让最相关结果排前面”。
- 标题改写：重点是“让文档块更容易被检索命中”。

### 2. 从 ACP 考试上记忆

- 如果题目强调“召回后内容太碎”，优先想到句子窗口检索或自动合并检索。
- 如果题目强调“召回到了但排序不准”，优先想到重排序。
- 如果题目强调“块本身表达弱、不容易命中”，优先想到标题改写。

### 3. 从当前 C2 课内复习上区分

- 句子窗口检索、重排序、标题改写，更适合作为当前课内与考纲都能接受的复习点。
- 自动合并检索更适合作为考纲扩展理解来记，不要误当成当前 C2_2.5 课内必须逐字背诵的原词。
```

- [ ] **Step 4: 写入速记提示**

在文档结尾补上速记法：

```md
## 速记提示

- 想“召回更多上下文”：句子窗口检索
- 想“把碎片拼完整”：自动合并检索
- 想“让排序更准”：重排序
- 想“让块更容易被召回”：标题改写
```

### Task 2: 校对与验证

**Files:**
- Verify: `.trae/specs/generate-c2-mock-exam/rag-optimization-comparison.md`

- [ ] **Step 1: 检查结构完整**

确认文件包含以下区块：

```text
# RAG 优化方法对比表
> 口径说明
| 概念 | 一句话定义 | ...
## 结论
## 速记提示
```

- [ ] **Step 2: 运行 Markdown 诊断**

检查文件：

```text
file:///Users/admin/openSource/aliyun_acp_learning/.trae/specs/generate-c2-mock-exam/rag-optimization-comparison.md
```

预期：

```text
无诊断错误
```

- [ ] **Step 3: 确认未改现有题库**

运行：

```bash
git diff -- . ':(exclude).trae/specs/generate-c2-mock-exam/rag-optimization-comparison.md' ':(exclude)docs/superpowers/specs/2026-06-11-rag-optimization-comparison-design.md' ':(exclude)docs/superpowers/plans/2026-06-11-rag-optimization-comparison.md'
```

预期：

```text
不包含本次新增对比文档之外的意外改动
```
