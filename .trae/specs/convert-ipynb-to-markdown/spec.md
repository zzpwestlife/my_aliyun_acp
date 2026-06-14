# Notebook 转 Markdown Spec

## Why
课程资料当前分散在多个 `.ipynb` 文件中，不利于统一阅读、检索和后续发布。需要将目标目录下全部 notebook 完整迁移为标准 Markdown 文件，同时保证内容与原始 notebook 完全一致。

## What Changes
- 遍历 `/Users/admin/openSource/aliyun_acp_learning/大模型ACP认证教程` 目录下全部 `.ipynb` 文件。
- 按相对路径与文件名的稳定顺序处理 notebook，保证迁移顺序可复现且符合课程内容递进。
- 将每个 `.ipynb` 独立转换为一个 `.md` 文件，统一输出到集中目录，并保留源目录结构镜像。
- 完整保留 notebook 中的 Markdown 文本、数学公式、代码单元、执行输出、图片引用和链接。
- 修正 Markdown 中的资源引用路径，确保在新目录结构下仍可正常访问。
- 产出逐文件验证结果，确认 Markdown 与原 notebook 内容无遗漏、无篡改、无格式错乱。

## Impact
- Affected specs: notebook 内容迁移、Markdown 导出、资源路径修正、完整性校验
- Affected code: 未来实现将涉及 notebook 解析脚本、Markdown 导出逻辑、资源路径处理逻辑、校验脚本，以及输出目录 `大模型ACP认证教程/markdown_export/`

## ADDED Requirements
### Requirement: 全量 Notebook 发现与排序
系统 SHALL 发现目标目录下的全部 `.ipynb` 文件，并按照稳定、可复现的逻辑顺序处理。

#### Scenario: 按课程结构顺序处理
- **WHEN** 系统扫描 `/Users/admin/openSource/aliyun_acp_learning/大模型ACP认证教程`
- **THEN** 系统包含该目录下全部 `.ipynb` 文件
- **THEN** 系统按相对路径和文件名升序形成处理列表
- **THEN** 同一执行条件下得到相同的处理顺序

### Requirement: 独立 Markdown 镜像导出
系统 SHALL 为每个源 notebook 生成一个独立的 Markdown 文件，并输出到集中目录 `大模型ACP认证教程/markdown_export/` 下的镜像路径中。

#### Scenario: 生成镜像目录中的 Markdown
- **WHEN** 系统处理任意一个源 notebook
- **THEN** 在 `markdown_export/` 中创建与源目录一致的相对路径
- **THEN** 生成与源文件同名、扩展名为 `.md` 的目标文件
- **THEN** 不将多个 notebook 合并为单一 Markdown 文件

### Requirement: 内容完全等价迁移
系统 SHALL 将每个 notebook 的全部原始内容按单元顺序完整迁移到对应 Markdown 文件，不得遗漏、改写或重排内容。

#### Scenario: 保留单元内容与顺序
- **WHEN** 系统转换 notebook
- **THEN** Markdown 单元、代码单元与输出内容的顺序与源 notebook 一致
- **THEN** 原始 Markdown 文本、数学公式、代码内容被完整保留
- **THEN** 文本语义、代码文本、输出文本和可引用资源标识不被篡改

#### Scenario: 保留执行输出
- **WHEN** notebook 单元包含执行结果
- **THEN** 文本输出、富文本输出、图片输出或其引用被完整迁移
- **THEN** 目标 Markdown 中可以明确区分代码内容与执行结果

### Requirement: 资源引用路径可用
系统 SHALL 修正导出后 Markdown 中的资源路径与链接引用，使其在集中目录结构下保持可访问。

#### Scenario: 修正本地资源相对路径
- **WHEN** notebook 或其导出内容引用本地图片或附件
- **THEN** 目标 Markdown 中的相对路径指向导出后实际可访问的位置
- **THEN** 路径格式符合标准 Markdown 语法

#### Scenario: 保留外部链接
- **WHEN** notebook 内容包含外部 URL
- **THEN** 目标 Markdown 保留原始外部链接目标
- **THEN** 链接语法符合标准 Markdown 规范

### Requirement: 完整性校验
系统 SHALL 在导出完成后对每个 notebook 与对应 Markdown 执行完整性校验，并报告任何缺失、错漏或格式异常。

#### Scenario: 导出校验通过
- **WHEN** 系统完成全部 Markdown 导出
- **THEN** 校验覆盖每一个已发现的 `.ipynb`
- **THEN** 校验结果确认无遗漏单元、无缺失输出、无资源引用断裂
- **THEN** 生成可供人工复核的逐文件校验结论
