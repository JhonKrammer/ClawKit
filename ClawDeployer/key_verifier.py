#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Key验证模块

负责验证用户输入的Key是否符合格式要求。
目前仅进行本地格式校验，不与服务器进行验证。

Author: ClawKit Team
Date: 2026-03-20
"""

import re


class KeyVerifier:
    """
    Key验证器类，用于验证Key的格式是否正确
    """
    
    def __init__(self):
        """
        初始化Key验证器
        """
        # Key格式正则表达式：CLAW-YYYYMMDD-XXXXXXXXXXXX
        # 其中：
        # CLAW- 固定前缀
        # YYYYMMDD 日期格式
        # XXXXXXXXXX 10位字母数字组合
        self.key_pattern = r'^CLAW-\d{8}-[A-Z0-9]{10,20}$'
    
    def validate_key_format(self, key):
        """
        验证Key格式是否正确
        
        Args:
            key (str): 用户输入的Key
            
        Returns:
            bool: Key格式是否正确
        """
        if not key:
            return False
        
        # 使用正则表达式验证Key格式
        match = re.match(self.key_pattern, key)
        return bool(match)
    
    def get_key_info(self, key):
        """
        从Key中提取信息
        
        Args:
            key (str): 有效的Key
            
        Returns:
            dict: Key信息，包括日期和随机部分
        """
        if not self.validate_key_format(key):
            return None
        
        parts = key.split('-')
        if len(parts) != 3:
            return None
        
        return {
            'prefix': parts[0],
            'date': parts[1],
            'random': parts[2]
        }
    
    def is_valid_key(self, key):
        """
        验证Key是否有效
        
        注意：目前仅验证格式，不与服务器验证
        
        Args:
            key (str): 用户输入的Key
            
        Returns:
            bool: Key是否有效
        """
        # 仅验证格式
        return self.validate_key_format(key)
