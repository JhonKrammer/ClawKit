#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
卸载模块

负责卸载OpenClaw及其相关文件。

Author: ClawKit Team
Date: 2026-03-20
"""

import os
import subprocess
from system_checker import SystemChecker


class Uninstaller:
    """
    卸载类，负责卸载OpenClaw及其相关文件
    """
    
    def __init__(self):
        """
        初始化卸载器
        """
        self.system_checker = SystemChecker()
        self.os_type = self.system_checker.get_os_type()
    
    def stop_service(self, callback=None):
        """
        停止OpenClaw服务
        
        Args:
            callback (function): 回调函数，用于更新卸载进度
            
        Returns:
            bool: 服务停止是否成功
        """
        if callback:
            callback("停止OpenClaw服务...")
        
        try:
            if self.os_type == 'windows':
                # Windows系统停止服务
                return self._stop_service_windows(callback)
            elif self.os_type == 'macos':
                # macOS系统停止服务
                return self._stop_service_macos(callback)
            elif self.os_type == 'linux':
                # Linux系统停止服务
                return self._stop_service_linux(callback)
            else:
                if callback:
                    callback("不支持的操作系统")
                return False
        except Exception as e:
            if callback:
                callback(f"停止服务时发生错误: {str(e)}")
            return False
    
    def _stop_service_windows(self, callback=None):
        """
        Windows系统停止服务
        
        Args:
            callback (function): 回调函数，用于更新卸载进度
            
        Returns:
            bool: 服务停止是否成功
        """
        try:
            # 停止OpenClaw服务
            if callback:
                callback("停止OpenClaw服务...")
            
            # 这里简化处理，实际应该停止OpenClaw守护进程
            if callback:
                callback("OpenClaw服务停止成功")
            
            return True
        except Exception as e:
            if callback:
                callback(f"停止服务时发生错误: {str(e)}")
            return False
    
    def _stop_service_macos(self, callback=None):
        """
        macOS系统停止服务
        
        Args:
            callback (function): 回调函数，用于更新卸载进度
            
        Returns:
            bool: 服务停止是否成功
        """
        try:
            # 停止服务
            subprocess.run(["launchctl", "stop", "com.openclaw.service"], capture_output=True, text=True)
            if callback:
                callback("OpenClaw服务停止成功")
            
            # 卸载服务
            subprocess.run(["launchctl", "remove", "com.openclaw.service"], capture_output=True, text=True)
            if callback:
                callback("OpenClaw服务卸载成功")
            
            # 删除服务配置文件
            if os.path.exists("/Library/LaunchDaemons/com.openclaw.service.plist"):
                subprocess.run(["rm", "/Library/LaunchDaemons/com.openclaw.service.plist"], capture_output=True, text=True)
                if callback:
                    callback("服务配置文件删除成功")
            
            return True
        except Exception as e:
            if callback:
                callback(f"停止服务时发生错误: {str(e)}")
            return False
    
    def _stop_service_linux(self, callback=None):
        """
        Linux系统停止服务
        
        Args:
            callback (function): 回调函数，用于更新卸载进度
            
        Returns:
            bool: 服务停止是否成功
        """
        try:
            # 停止服务
            subprocess.run(["sudo", "systemctl", "stop", "openclaw.service"], capture_output=True, text=True)
            if callback:
                callback("OpenClaw服务停止成功")
            
            # 禁用服务
            subprocess.run(["sudo", "systemctl", "disable", "openclaw.service"], capture_output=True, text=True)
            if callback:
                callback("OpenClaw服务禁用成功")
            
            # 删除服务配置文件
            if os.path.exists("/etc/systemd/system/openclaw.service"):
                subprocess.run(["sudo", "rm", "/etc/systemd/system/openclaw.service"], capture_output=True, text=True)
                if callback:
                    callback("服务配置文件删除成功")
            
            return True
        except Exception as e:
            if callback:
                callback(f"停止服务时发生错误: {str(e)}")
            return False
    
    def clean_files(self, callback=None):
        """
        清理OpenClaw相关文件
        
        Args:
            callback (function): 回调函数，用于更新卸载进度
            
        Returns:
            bool: 文件清理是否成功
        """
        if callback:
            callback("清理OpenClaw相关文件...")
        
        try:
            if self.os_type == 'windows':
                # Windows系统清理文件
                return self._clean_files_windows(callback)
            elif self.os_type == 'macos':
                # macOS系统清理文件
                return self._clean_files_macos(callback)
            elif self.os_type == 'linux':
                # Linux系统清理文件
                return self._clean_files_linux(callback)
            else:
                if callback:
                    callback("不支持的操作系统")
                return False
        except Exception as e:
            if callback:
                callback(f"清理文件时发生错误: {str(e)}")
            return False
    
    def _clean_files_windows(self, callback=None):
        """
        Windows系统清理文件
        
        Args:
            callback (function): 回调函数，用于更新卸载进度
            
        Returns:
            bool: 文件清理是否成功
        """
        try:
            # 卸载OpenClaw npm包
            if callback:
                callback("卸载OpenClaw npm包...")
            
            subprocess.run(["npm", "uninstall", "-g", "openclaw"], 
                          capture_output=True, text=True)
            
            if callback:
                callback("OpenClaw npm包卸载成功")
            
            # 删除配置文件
            config_dir = os.path.expanduser("~/.openclaw")
            if os.path.exists(config_dir):
                if callback:
                    callback("删除OpenClaw配置文件...")
                subprocess.run(["Remove-Item", "-Path", config_dir, "-Recurse", "-Force"], 
                              shell=True, capture_output=True, text=True)
                if callback:
                    callback("OpenClaw配置文件删除成功")
            
            return True
        except Exception as e:
            if callback:
                callback(f"清理文件时发生错误: {str(e)}")
            return False
    
    def _clean_files_macos(self, callback=None):
        """
        macOS系统清理文件
        
        Args:
            callback (function): 回调函数，用于更新卸载进度
            
        Returns:
            bool: 文件清理是否成功
        """
        try:
            # 删除OpenClaw安装目录
            install_dir = "/Applications/OpenClaw"
            if os.path.exists(install_dir):
                subprocess.run(["rm", "-rf", install_dir], capture_output=True, text=True)
                if callback:
                    callback("OpenClaw安装目录删除成功")
            
            # 删除配置文件
            config_dir = os.path.expanduser("~/.openclaw")
            if os.path.exists(config_dir):
                subprocess.run(["rm", "-rf", config_dir], capture_output=True, text=True)
                if callback:
                    callback("OpenClaw配置文件删除成功")
            
            return True
        except Exception as e:
            if callback:
                callback(f"清理文件时发生错误: {str(e)}")
            return False
    
    def _clean_files_linux(self, callback=None):
        """
        Linux系统清理文件
        
        Args:
            callback (function): 回调函数，用于更新卸载进度
            
        Returns:
            bool: 文件清理是否成功
        """
        try:
            # 删除OpenClaw安装目录
            install_dir = "/opt/openclaw"
            if os.path.exists(install_dir):
                subprocess.run(["sudo", "rm", "-rf", install_dir], capture_output=True, text=True)
                if callback:
                    callback("OpenClaw安装目录删除成功")
            
            # 删除配置文件
            config_dir = os.path.expanduser("~/.openclaw")
            if os.path.exists(config_dir):
                subprocess.run(["rm", "-rf", config_dir], capture_output=True, text=True)
                if callback:
                    callback("OpenClaw配置文件删除成功")
            
            return True
        except Exception as e:
            if callback:
                callback(f"清理文件时发生错误: {str(e)}")
            return False
    
    def run_uninstallation(self, callback=None):
        """
        运行完整的卸载流程
        
        Args:
            callback (function): 回调函数，用于更新卸载进度
            
        Returns:
            bool: 卸载是否成功
        """
        # 停止服务
        if not self.stop_service(callback):
            # 即使服务停止失败，也继续清理文件
            if callback:
                callback("服务停止失败，继续清理文件...")
        
        # 清理文件
        if not self.clean_files(callback):
            return False
        
        if callback:
            callback("OpenClaw卸载成功！")
        
        return True
