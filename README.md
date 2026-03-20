# ClawKit

## 项目概述

ClawKit 是一个用于简化 OpenClaw 部署和卸载的可视化工具，提供一键安装和卸载功能，支持 Windows、macOS 和 Linux 三大操作系统。

## 功能特性

### 核心功能
- **一键部署**：自动检测系统环境，安装依赖，配置 OpenClaw
- **一键卸载**：彻底清理 OpenClaw 及其相关文件
- **Key 验证**：使用单次有效的 Key 进行身份验证
- **跨平台支持**：支持 Windows、macOS 和 Linux
- **错误处理**：提供详细的错误信息和处理建议

### 系统要求
- **Windows**：Windows 10/11 (64位)
- **macOS**：macOS 10.15及以上
- **Linux**：Ubuntu 18.04+、Debian 10+、CentOS 7+等主流Linux发行版
- **Python**：3.10+

## 安装说明

1. **下载安装包**：从官方网站或 GitHub 下载对应操作系统的安装包
2. **运行安装程序**：双击安装包，按照提示操作
3. **输入 Key**：在提示界面输入有效的 Key
4. **等待安装完成**：安装程序会自动完成依赖安装和 OpenClaw 配置
5. **启动 OpenClaw**：安装完成后，OpenClaw 会自动启动

## 卸载说明

1. **运行卸载程序**：在开始菜单或应用程序文件夹中找到卸载程序
2. **输入 Key**：在提示界面输入有效的 Key
3. **等待卸载完成**：卸载程序会自动停止服务并清理文件
4. **确认卸载**：卸载完成后，会显示卸载成功信息

## Key 管理

Key 由后台管理系统生成，具有以下特性：
- **单次有效**：每个 Key 只能使用一次
- **时效性**：Key 有一定的有效期（例如24小时）
- **格式**：20-30位的字母数字组合，例如：`CLAW-20260320-ABC123DEF456`

## 技术实现

- **开发语言**：Python 3.10+
- **界面库**：Tkinter
- **网络库**：requests
- **系统操作**：subprocess
- **打包工具**：PyInstaller

## 项目结构

```
ClawDeployer/
├── main.py              # 主程序
├── install.py           # 安装模块
├── uninstall.py         # 卸载模块
├── key_verifier.py      # Key验证模块
├── system_checker.py    # 系统检测模块
├── gui/                 # 界面相关
│   ├── main_window.py
│   ├── key_input.py
│   ├── progress_window.py
│   └── result_window.py
├── utils/               # 工具函数
│   ├── logger.py
│   └── config.py
└── requirements.txt     # 依赖文件
```

## 贡献指南

欢迎贡献代码、报告问题或提出建议。请通过 GitHub Issues 或 Pull Requests 参与项目。

## 许可证

本项目采用 MIT 许可证。详见 LICENSE 文件。

## 联系方式

- **官方网站**：https://openclaw.io
- **GitHub**：https://github.com/openclaw/clawkit
- **邮箱**：contact@openclaw.io
