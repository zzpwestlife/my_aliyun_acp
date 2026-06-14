# Tasks
- [x] Task 1: 确认输入范围与输出结构
  - [x] 盘点 `/Users/admin/openSource/aliyun_acp_learning/大模型ACP认证教程` 下全部 `.ipynb` 文件
  - [x] 按相对路径与文件名升序生成稳定处理清单
  - [x] 确认集中输出目录为 `大模型ACP认证教程/markdown_export/`，并保留源目录结构镜像

- [x] Task 2: 实现 notebook 到 Markdown 的逐文件导出
  - [x] 为每个 `.ipynb` 生成一个独立 `.md` 文件
  - [x] 保留全部 Markdown 文本、数学公式、代码块与单元顺序
  - [x] 保留执行输出内容，包括文本输出、富文本输出、图片输出或图片引用

- [x] Task 3: 修正资源路径与链接
  - [x] 检查导出后的图片、附件、相对链接和外部链接
  - [x] 将本地资源引用调整为适配 `markdown_export/` 镜像目录的标准 Markdown 路径
  - [x] 确保外部链接在内容与语法上保持原样可用

- [x] Task 4: 完整性验证与差异排查
  - [x] 逐文件比对 notebook 与对应 Markdown 的单元顺序和内容覆盖情况
  - [x] 检查是否存在遗漏单元、遗漏输出、公式丢失、代码块错位或格式错乱
  - [x] 检查所有资源引用是否可访问，并记录异常

- [x] Task 5: 交付最终整理结果
  - [x] 确认全部 `.ipynb` 都已生成对应 `.md`
  - [x] 输出最终处理结果与验证结论
  - [x] 确保用户可按镜像目录直接浏览整理后的全部 Markdown 文档

# Task Dependencies
- Task 2 depends on Task 1
- Task 3 depends on Task 2
- Task 4 depends on Task 2
- Task 5 depends on Task 3
- Task 5 depends on Task 4
