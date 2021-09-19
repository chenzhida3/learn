# -*- encoding: utf-8 -*-
'''
@File    : serializer.py
@Time    : 2021/9/19 16:35
@Author  : Chenzd
@Software: PyCharm
序列化器
'''
from rest_framework import serializers


class ProjectSerializer(serializers.Serializer):
    """
    创建项目序列化器类
    """
    id = serializers.IntegerField(label='ID', read_only=True)
    name = serializers.CharField(label='项目名称', max_length=255, help_text='项目名称')
    leader = serializers.CharField(label='负责人', max_length=50, help_text='负责人')
    tester = serializers.CharField(label='测试人员', max_length=50, help_text='测试人员')
    programer = serializers.CharField(label='开发人员', max_length=50, help_text='开发人员')
    publish_app = serializers.CharField(label='发布应用', max_length=200, help_text='发布应用')
    # null设置数据库中此字段允许为空   blank设置前端可以不传值   default设置默认值
    desc = serializers.CharField(label='简要描述', help_text='简要描述', allow_blank=True, default='', allow_null=True)
