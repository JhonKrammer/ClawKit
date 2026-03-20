#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
进度窗口界面

用于显示安装或卸载的进度信息。

Author: ClawKit Team
Date: 2026-03-20
"""

import tkinter as tk


class ProgressWindow:
    """
    进度窗口类，用于显示安装或卸载的进度信息
    """
    
    def __init__(self, parent, action_type):
        """
        初始化进度窗口
        
        Args:
            parent: 父窗口
            action_type: 操作类型，"安装"或"卸载"
        """
        self.parent = parent
        self.action_type = action_type
        
        # 创建窗口
        self.window = tk.Toplevel(parent)
        self.window.title(f"{action_type}进度")
        self.window.geometry("500x300")
        self.window.resizable(False, False)
        
        # 居中窗口
        self.center_window()
        
        # 创建组件
        self.create_widgets()
        
        # 禁用父窗口
        self.parent.attributes("-disabled", True)
        
        # 设置窗口关闭事件
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)
    
    def center_window(self):
        """
        居中窗口
        """
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f"{width}x{height}+{x}+{y}")
    
    def create_widgets(self):
        """
        创建窗口组件
        """
        # 创建标题
        title_label = tk.Label(self.window, text=f"{self.action_type}中...", 
                              font=("Arial", 14, "bold"))
        title_label.pack(pady=20)
        
        # 创建进度条
        self.progress_var = tk.DoubleVar()
        self.progress_bar = tk.Scale(self.window, variable=self.progress_var, 
                                    orient=tk.HORIZONTAL, length=400, 
                                    from_=0, to=100, showvalue=False)
        self.progress_bar.pack(pady=10)
        
        # 创建日志文本框
        self.log_text = tk.Text(self.window, width=60, height=10, 
                              font=("Arial", 10))
        self.log_text.pack(pady=10)
        self.log_text.config(state=tk.DISABLED)
        
        # 创建状态标签
        self.status_label = tk.Label(self.window, text="准备开始...", 
                                   font=("Arial", 10))
        self.status_label.pack(pady=5)
    
    def update_progress(self, message):
        """
        更新进度信息
        
        Args:
            message: 进度消息
        """
        # 更新日志
        self.log_text.config(state=tk.NORMAL)
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.log_text.config(state=tk.DISABLED)
        
        # 更新状态标签
        self.status_label.config(text=message)
        
        # 更新窗口
        self.window.update()
    
    def close(self):
        """
        关闭窗口
        """
        # 启用父窗口
        self.parent.attributes("-disabled", False)
        
        # 关闭窗口
        self.window.destroy()
    
    def on_close(self):
        """
        处理窗口关闭事件
        """
        # 禁用关闭按钮
        pass
