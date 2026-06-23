# 整理 exam_materials 目录 Spec

## Why
当前 `/Users/admin/openSource/aliyun_acp_learning/exam_materials` 目录下的文件存在多层嵌套（如 `outline`, `questions`, `answers`, `extra` 等子目录），且包含各种临时文件与多余的变体文件。用户要求每个章节（chapter）目录内仅保留三份核心文件，且格式规范、命名统一为 PDF 格式，多余文件需进行归档清理，以方便查阅和打印。

## What Changes
- 展平 C2、C3、C4 目录，取消内部的 `outline`, `questions`, `answers`, `extra` 等子目录层级。
- 选定每个章节对应的 3 份核心文件：
  - 考试大纲（如原 `[章节]_考试大纲梳理.md`）
  - 模拟题题目（如原 `[章节]_模拟题_仅客观题.md` 或 `[章节]_模拟题_仅题目.md`）
  - 模拟题答案解析（如原 `[章节]_模拟题_客观题含答案.md`）
- 将上述 3 份核心 Markdown 文件转换为 PDF 格式。
- 将文件重命名为规范格式：`[章节编号]_考试大纲.pdf`、`[章节编号]_模拟题题目.pdf`、`[章节编号]_模拟题答案解析.pdf`。
- 将其余多余文件、临时文件统一移动至 `exam_materials/archive/` 目录归档存储。

## Impact
- Affected specs: 规范化考试资料的交付格式。
- Affected code: `/Users/admin/openSource/aliyun_acp_learning/exam_materials` 目录结构与文件类型将大幅改变。

## ADDED Requirements
### Requirement: 文件筛选与格式转换
系统应筛选出最核心的 3 份 Markdown 文件，并将其转换为 PDF 格式。

#### Scenario: 转换与重命名
- **WHEN** 脚本运行处理 C2 目录时
- **THEN** 生成 `C2_考试大纲.pdf`、`C2_模拟题题目.pdf`、`C2_模拟题答案解析.pdf`，并存放在 `C2` 根目录下。

### Requirement: 冗余文件归档
系统应将未被选为核心 3 份的 Markdown 等文件移动至独立的归档目录（如 `archive`），确保各章节根目录下只有指定的 3 个 PDF 文件。
