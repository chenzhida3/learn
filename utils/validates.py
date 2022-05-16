#!/usr/bin/env python
"""
-*- coding: utf-8 -*-
@Time    : 2022/5/16 16:06
@Author  : Chenzhida
@Email   : chenzhida3@163.com
@File    : validates.py
@Describe: 自定义校验器
@License : Copyright SideWalk Group © 2020~2022.All Rights Reserved
"""
from rest_framework import serializers
from projects.models import Projects
from interfaces.models import Interfaces


def whether_existed_project_id(value):
    """
    检查项目id是否存在
    """
    if not isinstance(value, int):
        raise serializers.ValidationError('所选项目有误！')
    elif not Projects.objects.filter(is_delete=False, id=value).exists():
        raise serializers.ValidationError('所选项目不存在！')


def whether_existed_interface_id(value):
    '''
    检查接口id是否存在
    '''
    if not isinstance(value, int):
        raise serializers.ValidationError('所选接口有误！')
    elif not Interfaces.objects.filter(is_delete=False, id=value).exists():
        raise serializers.ValidationError("所选接口不存在！")