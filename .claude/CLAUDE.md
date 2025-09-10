# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# 所有交互回答都使用中文

# 启动并行的代理执行任务

# 搜索约定
- 如需简单字符串匹配 → Grep
- 如需结构化/跨语言模式匹配 → 请优先使用 Bash(ast-grep …)，示例：
  Bash(ast-grep -p '$FUNC($ARG)' src/)

# 环境约定
- python环境：python3 pip3
- nodejs环境：node npm
- docker环境：docker%

# 项目概述
这是一个Python学习项目，按照功能模块组织成不同的目录结构。项目包含Python基础功能学习代码，包括函数定义、高级特性、面向对象编程、异常处理、网络编程、数据库操作和Web开发。

# 项目结构
- `1.function/` - Python函数定义和使用示例
- `2. advanced_feature/` - Python高级特性（迭代、切片等）
- `3. obejct_oriented/` - 面向对象编程示例
- `4. exception_handle/` - 异常处理和错误处理
- `5. internet/` - 网络编程（TCP、邮件等）
- `6. db/` - 数据库操作（SQLite）
- `7.web/` - Web开发（Flask应用）

# 运行命令
- 运行单个Python文件：`python 文件路径.py`
- 运行Flask应用：`python 7.web/app.py`
- 运行SQLite数据库操作：`python 6.db/sql_lite.py`

# 技术栈
- Python 3.x
- Flask（Web框架）
- SQLite（数据库）
- Socket（网络编程）

# 注意事项
- 代码示例中存在一些语法错误，如`6. db/sql_lite.py`第8行和第14行有拼写错误
- `7.web/app.py`中有重复的路由定义，需要修正
- 网络编程示例中存在语法错误需要修复