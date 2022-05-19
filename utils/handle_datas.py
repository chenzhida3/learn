#!/usr/bin/env python
"""
-*- coding: utf-8 -*-
@Time    : 2022/5/16 16:57
@Author  : Chenzhida
@Email   : chenzhida3@163.com
@File    : handle_datas.py
@Describe: 数据格式处理
@License : Copyright SideWalk Group © 2020~2022.All Rights Reserved
"""


def handle_param_type(value):
    """将传入的值获取它的类型"""
    if isinstance(value, int):
        param_type = 'int'
    elif isinstance(value, float):
        param_type = 'float'
    elif isinstance(value, bool):
        param_type = 'boolean'
    else:
        param_type = 'string'
    return param_type


def handle_data2(datas):
    """
    处理第3中类型的数据格式
    将[{"age":18},...]
    处理成[key:"age", value:18, param_type:'int']
    """
    result_list = []
    if datas is not None:
        for key, value in datas.items():

            result_list.append({
                "key": key,
                "value": value,
                "param_type": handle_param_type(value)
            })
    return result_list


def handle_data4(datas):
    """
    处理第四种类型的数据格式
    将["Content-Type": "application/json","Connection": "keep-alive"]
    转化为 [{key:"Content-Type", value:"application/json"},]
    """
    result_list = []
    if datas is not None:
        for key, value in datas.items():
            result_list.append({
                "key": key,
                "value": value
            })
    return result_list

