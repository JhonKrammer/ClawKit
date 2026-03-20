#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
系统检测模块

负责检测操作系统类型和版本，为后续的安装和卸载操作提供依据。

Author: ClawKit Team
Date: 2026-03-20
"""

import platform
import sys


class SystemChecker:
    """
    系统检测类，用于检测操作系统类型和版本
    """
    
    def __init__(self):
        """
        初始化系统检测器
        """
        self.system = platform.system()
        self.release = platform.release()
        self.version = platform.version()
        self.machine = platform.machine()
    
    def get_os_info(self):
        """
        获取操作系统信息
        
        Returns:
            dict: 操作系统信息，包括类型、版本等
        """
        return {
            'system': self.system,
            'release': self.release,
            'version': self.version,
            'machine': self.machine
        }
    
    def is_windows(self):
        """
        检测是否为Windows系统
        
        Returns:
            bool: 是否为Windows系统
        """
        return self.system == 'Windows'
    
    def is_macos(self):
        """
        检测是否为macOS系统
        
        Returns:
            bool: 是否为macOS系统
        """
        return self.system == 'Darwin'
    
    def is_linux(self):
        """
        检测是否为Linux系统
        
        Returns:
            bool: 是否为Linux系统
        """
        return self.system == 'Linux'
    
    def get_os_type(self):
        """
        获取操作系统类型
        
        Returns:
            str: 操作系统类型，'windows'、'macos'或'linux'
        """
        if self.is_windows():
            return 'windows'
        elif self.is_macos():
            return 'macos'
        elif self.is_linux():
            return 'linux'
        else:
            return 'unknown'
    
    def is_supported(self):
        """
        检测当前操作系统是否支持
        
        Returns:
            bool: 是否支持
        """
        os_type = self.get_os_type()
        if os_type == 'unknown':
            return False
        
        # 检查具体版本
        if os_type == 'windows':
            # 检查是否为Windows 10或11
            try:
                version = int(self.release.split('.')[0])
                return version >= 10
            except:
                return False
        elif os_type == 'macos':
            # 检查是否为macOS 10.15或以上
            try:
                parts = self.release.split('.')
                if len(parts) >= 2:
                    major = int(parts[0])
                    minor = int(parts[1])
                    return (major == 10 and minor >= 15) or major > 10
                return False
            except:
                return False
        elif os_type == 'linux':
            # 对于Linux，我们假设主流发行版都支持
            return True
        
        return False
    
    def get_supported_os_info(self):
        """
        获取支持的操作系统信息
        
        Returns:
            str: 支持的操作系统信息
        """
        return (
            "支持的操作系统：\n"
            "- Windows: Windows 10/11 (64位)\n"
            "- macOS: macOS 10.15及以上\n"
            "- Linux: Ubuntu 18.04+, Debian 10+, CentOS 7+等主流Linux发行版"
        )
