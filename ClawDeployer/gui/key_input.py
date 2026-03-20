#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Key输入窗口界面

用于用户输入Key并验证其格式是否正确。

Author: ClawKit Team
Date: 2026-03-20
"""

import tkinter as tk
from tkinter import messagebox
from key_verifier import KeyVerifier


class KeyInputWindow:
    """
    Key输入窗口类，用于用户输入Key并验证
    """
    
    def __init__(self, parent, action_type, callback):
        """
        初始化Key输入窗口
        
        Args:
            parent: 父窗口
            action_type: 操作类型，"安装"或"卸载"
            callback: 验证成功后的回调函数
        """
        self.parent = parent
        self.action_type = action_type
        self.callback = callback
        self.key_verifier = KeyVerifier()
        
        # 创建窗口
        self.window = tk.Toplevel(parent)
        self.window.title(f"{action_type} - 输入Key")
        self.window.geometry("400x250")
        self.window.resizable(False, False)
        
        # 居中窗口
        self.center_window()
        
        # 创建组件
        self.create_widgets()
        
        # 聚焦到输入框
        self.key_entry.focus_set()
    
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
        title_label = tk.Label(self.window, text=f"请输入{self.action_type}Key", 
                              font=("Arial", 14, "bold"))
        title_label.pack(pady=20)
        
        # 创建Key输入框架
        input_frame = tk.Frame(self.window)
        input_frame.pack(pady=10)
        
        # Key标签
        key_label = tk.Label(input_frame, text="Key:", font=("Arial", 12))
        key_label.pack(side=tk.LEFT, padx=10)
        
        # Key输入框
        self.key_entry = tk.Entry(input_frame, width=30, font=("Arial", 12))
        self.key_entry.pack(side=tk.LEFT, padx=10)
        
        # 提示信息
        hint_label = tk.Label(self.window, text="Key格式: CLAW-YYYYMMDD-XXXXXXXXXXXX", 
                             font=("Arial", 10, "italic"))
        hint_label.pack(pady=5)
        
        # 按钮框架
        button_frame = tk.Frame(self.window)
        button_frame.pack(pady=20)
        
        # 验证按钮
        verify_button = tk.Button(button_frame, text="验证", 
                                command=self.on_verify, 
                                width=10, height=1, 
                                font=("Arial", 12))
        verify_button.pack(side=tk.LEFT, padx=10)
        
        # 取消按钮
        cancel_button = tk.Button(button_frame, text="取消", 
                                command=self.window.destroy, 
                                width=10, height=1, 
                                font=("Arial", 12))
        cancel_button.pack(side=tk.RIGHT, padx=10)
    
    def on_verify(self):
        """
        处理验证按钮点击事件
        """
        # 获取输入的Key
        key = self.key_entry.get().strip()
        
        # 验证Key格式
        if not self.key_verifier.is_valid_key(key):
            messagebox.showerror("错误", "Key格式不正确，请检查输入的Key。")
            return
        
        # 验证成功，调用回调函数
        self.callback(key)
        
        # 关闭窗口
        self.window.destroy()
