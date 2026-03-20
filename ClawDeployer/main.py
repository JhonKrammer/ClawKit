#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ClawDeployer 主程序

这是 ClawDeployer 的主入口文件，负责启动应用程序并协调各个模块的工作。

Author: ClawKit Team
Date: 2026-03-20
"""

import sys
import os
import tkinter as tk
from tkinter import messagebox

# 添加当前目录到系统路径，以便导入其他模块
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from gui.main_window import MainWindow


def main():
    """
    主函数，启动 ClawDeployer 应用程序
    """
    try:
        # 创建主窗口
        root = tk.Tk()
        root.title("ClawDeployer - OpenClaw 部署工具")
        root.geometry("600x400")
        root.resizable(False, False)
        
        # 创建应用实例
        app = MainWindow(root)
        
        # 启动主循环
        root.mainloop()
        
    except Exception as e:
        # 捕获并显示错误信息
        messagebox.showerror("错误", f"启动应用程序时发生错误: {str(e)}")
        print(f"错误: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
