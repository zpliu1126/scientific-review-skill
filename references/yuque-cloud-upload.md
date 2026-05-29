# Yuque MCP 上传云文档注意事项

Use these rules when publishing literature cards, evidence notes, or review outputs to a Yuque knowledge base through Yuque MCP or the Yuque API. The goal is to keep cloud publishing auditable without filling the conversation context with full document bodies.

## 推荐上传流程

1. 获取当前 Yuque 用户信息。

   先调用:

   ```text
   yuque_get_user
   ```

   记录返回结果中的 `login`。创建知识库、构造 namespace 和后续 API 路径都需要 Yuque login。

   Example:

   ```text
   login = zpliu
   ```

2. 创建知识库。

   使用:

   ```text
   yuque_create_book
   ```

   默认创建私有知识库，除非用户明确要求公开。创建后必须记录:

   ```text
   login
   book slug
   namespace = login/book_slug
   ```

   Example:

   ```text
   知识库名称: 氮响应途径
   namespace: zpliu/nitrogen-response-pathway
   ```

3. 创建文档。

   可以先用 MCP 上传第 1 篇文档，验证账号、知识库、权限和正文格式是否正常:

   ```text
   yuque_create_doc
   ```

   If `yuque_create_doc` returns full `body` or `body_html`, do not continue bulk uploading large documents through MCP in a way that prints full responses into the conversation. For batch uploads, prefer the Yuque API or a thin script that prints only minimal status lines:

   ```text
   CREATED title slug id
   SKIPPED title slug id
   FAILED title slug error
   ```

   Do not print full document bodies or `body_html` in batch upload logs.

4. 核对文档列表。

   上传后调用:

   ```text
   yuque_list_docs
   ```

   Confirm that the knowledge base contains the expected document count and that each target document has `title`, `slug`, and `id`.

5. 核对并修复目录树 TOC。

   `yuque_list_docs` can see documents that are not visible in the knowledge base directory tree. Always call:

   ```text
   yuque_get_toc
   ```

   If documents exist but are missing from the TOC, call:

   ```text
   yuque_update_toc
   ```

   Append missing documents as `DOC` nodes at the root level or under the user-specified target directory.

   Real failure pattern:

   ```text
   yuque_list_docs 显示有 10 篇文档
   yuque_get_toc 只显示第 1 篇
   ```

   Fix:

   ```text
   use yuque_update_toc to attach 002-010 to the root TOC
   rerun yuque_get_toc to confirm the final TOC count
   ```

## 已遇到的问题和解决办法

### 问题 1: 不知道 Yuque login

表现:

```text
创建知识库时需要 login，但一开始不知道当前账号 login
```

解决:

```text
先调用 yuque_get_user
login = 返回结果中的 login
```

Example:

```text
login = zpliu
```

### 问题 2: MCP 创建文档会回显整篇正文

表现:

```text
yuque_create_doc 成功后返回完整 body / body_html
输出非常长
占用大量上下文
```

原因:

```text
MCP 工具返回值包含完整文档正文
```

解决:

```text
只用 yuque_create_doc 上传第 1 篇测试文档
后续大批量文档改用 Yuque API 上传
最后再用 MCP 工具进行核对
```

要求:

```text
不要在对话中打印完整正文
不要让批量上传日志包含完整 body 或 body_html
```

### 问题 3: 本地 API 脚本首次联网失败

报错:

```text
getaddrinfo ENOTFOUND www.yuque.com
```

原因:

```text
沙箱或执行环境网络受限
```

解决:

```text
按权限要求重新以 escalated network 权限运行脚本
不要在未确认网络权限前反复修改 API 代码
```

### 问题 4: Yuque 文档列表返回结构不是裸数组

报错:

```text
TypeError: (existing.data || []).map is not a function
```

原因:

```text
脚本假设 existing.data 是数组
但实际返回结构可能是对象
文档列表可能位于 data、data.docs、data.items 等不同字段中
```

解决:

```js
const docs =
  Array.isArray(existing?.data) ? existing.data :
  Array.isArray(existing?.data?.docs) ? existing.data.docs :
  Array.isArray(existing?.data?.items) ? existing.data.items :
  Array.isArray(existing?.docs) ? existing.docs :
  Array.isArray(existing?.items) ? existing.items :
  [];
```

Rule:

```text
不要假设 Yuque API 返回的 data 一定是裸数组
```

### 问题 5: API 路径错误导致 404

报错:

```text
POST /api/v2/repos/zpliu%2Fnitrogen-response-pathway/docs failed: 404
```

原因:

```text
把 namespace 中的 / 整体 URL 编码成了 %2F
```

错误路径:

```text
/api/v2/repos/zpliu%2Fnitrogen-response-pathway/docs
```

正确做法:

```text
只分别编码 login 和 book_slug
保留路径中的 /
```

正确路径示例:

```text
/api/v2/repos/zpliu/nitrogen-response-pathway/docs
```

Rule:

```text
namespace = login/book_slug
API 路径中 login 和 book_slug 分别 encode
不要整体 encode namespace
```

### 问题 6: 文档已创建，但知识库目录只显示 1 篇

表现:

```text
yuque_list_docs 显示有 10 篇
yuque_get_toc 只显示第 1 篇
```

原因:

```text
批量 API 创建的后续文档没有自动挂到 TOC
```

解决:

```text
用 yuque_update_toc 把缺失文档逐个追加为 DOC 节点
可以先挂到目录根层级
修复后再次调用 yuque_get_toc 确认
```

Rule:

```text
上传完成后必须同时检查 yuque_list_docs 和 yuque_get_toc
不能只根据 yuque_list_docs 判断上传完成
```

## 最终检查标准

Only report `Yuque 文档上传完成` when all conditions are satisfied:

```text
1. yuque_list_docs 中能看到全部目标文档
2. yuque_get_toc 中能看到全部目标文档
3. 每篇文档都有 title、slug、id
4. TOC 中没有缺失文档
5. 没有未处理的 FAILED 文档
6. 已向用户打印最终上传报告
```

If documents have been created but the TOC is incomplete, report only:

```text
文档已创建，但目录树尚未完全修复。
```

Do not report:

```text
全部完成
```

## 最终输出报告模板

```text
Yuque 上传完成

用户: zpliu
知识库: 氮响应途径
namespace: zpliu/nitrogen-response-pathway

上传统计:
- 计划上传: 10 篇
- 新建成功: 9 篇
- 已存在跳过: 1 篇
- 上传失败: 0 篇

核对结果:
- yuque_list_docs: 10 篇
- yuque_get_toc 初次检查: 1 篇
- 已执行 TOC 修复: 是
- yuque_get_toc 最终检查: 10 篇

结论:
文档已全部上传，并已挂载到知识库目录树。
```
