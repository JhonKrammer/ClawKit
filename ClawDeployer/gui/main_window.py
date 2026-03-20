#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
主窗口界面

ClawDeployer的主界面，提供安装和卸载选项。

Author: ClawKit Team
Date: 2026-03-20
"""

import tkinter as tk
from tkinter import messagebox
from .key_input import KeyInputWindow
from .progress_window import ProgressWindow
from key_verifier import KeyVerifier
from install import Installer
from uninstall import Uninstaller


class MainWindow:
    """
    主窗口类，提供安装和卸载选项
    """
    
    def __init__(self, root):
        """
        初始化主窗口
        
        Args:
            root: tkinter根窗口
        """
        self.root = root
        self.key_verifier = KeyVerifier()
        self.installer = Installer()
        self.uninstaller = Uninstaller()
        
        # 创建主窗口组件
        self.create_widgets()
    
    def create_widgets(self):
        """
        创建主窗口组件
        """
        # 创建标题
        title_label = tk.Label(self.root, text="ClawDeployer - OpenClaw 部署工具", 
                              font=("Arial", 16, "bold"))
        title_label.pack(pady=20)
        
        # 创建描述
        desc_label = tk.Label(self.root, text="一键部署和卸载OpenClaw", 
                             font=("Arial", 12))
        desc_label.pack(pady=10)
        
        # 创建按钮框架
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=30)
        
        # 安装按钮
        install_button = tk.Button(button_frame, text="安装 OpenClaw", 
                                  command=self.on_install, 
                                  width=20, height=2, 
                                  font=("Arial", 12))
        install_button.pack(side=tk.LEFT, padx=10)
        
        # 卸载按钮
        uninstall_button = tk.Button(button_frame, text="卸载 OpenClaw", 
                                    command=self.on_uninstall, 
                                    width=20, height=2, 
                                    font=("Arial", 12))
        uninstall_button.pack(side=tk.RIGHT, padx=10)
        
        # 创建状态信息
        status_frame = tk.Frame(self.root)
        status_frame.pack(pady=20)
        
        status_label = tk.Label(status_frame, text="状态: 就绪", 
                               font=("Arial", 10))
        status_label.pack()
    
    def on_install(self):
        """
        处理安装按钮点击事件
        """
        # 打开Key输入窗口
        key_input_window = KeyInputWindow(self.root, "安装", self.on_key_verified_install)
    
    def on_uninstall(self):
        """
        处理卸载按钮点击事件
        """
        # 打开Key输入窗口
        key_input_window = KeyInputWindow(self.root, "卸载", self.on_key_verified_uninstall)
    
    def on_key_verified_install(self, key):
        """
        Key验证成功后的安装处理
        
        Args:
            key: 验证成功的Key
        """
        # 打开进度窗口
        progress_window = ProgressWindow(self.root, "安装")
        
        # 运行安装过程
        def install_callback(message):
            progress_window.update_progress(message)
        
        def install_finished(success):
            progress_window.close()
            if success:
                messagebox.showinfo("成功", "OpenClaw安装成功！")
            else:
                messagebox.showerror("失败", "OpenClaw安装失败，请查看日志了解详情。")
        
        # 在新线程中运行安装
        import threading
        install_thread = threading.Thread(
            target=lambda: install_finished(self.installer.run_installation(install_callback))
        )
        install_thread.daemon = True
        install_thread.start()
    
    def on_key_verified_uninstall(self, key):
        """
        Key验证成功后的卸载处理
        
        Args:
            key: 验证成功的Key
        """
        # 打开进度窗口
        progress_window = ProgressWindow(self.root, "卸载")
        
        # 运行卸载过程
        def uninstall_callback(message):
            progress_window.update_progress(message)
        
        def uninstall_finished(success):
            progress_window.close()
            if success:
                messagebox.showinfo("成功", "OpenClaw卸载成功！")
            else:
                messagebox.showerror("失败", "OpenClaw卸载失败，请查看日志了解详情。")
        
        # 在新线程中运行卸载
        import threading
        uninstall_thread = threading.Thread(
            target=lambda: uninstall_finished(self.uninstaller.run_uninstallation(uninstall_callback))
        )
        uninstall_thread.daemon = True
        uninstall_thread.start()
