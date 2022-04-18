# -*- encoding: utf-8 -*-
'''
@File    : serializer.py
@Time    : 2022/4/18 21:16
@Author  : Chenzd
@Software: PyCharm
内置函数序列化器
'''
from rest_framework import serializers
from debugtalks.models import Debugtalks


class DebugtalksSerializers(serializers.ModelSerializer):

    project = serializers.StringRelatedField(help_text='项目名称')
    class Meta:
        model = Debugtalks
        exclude = ('is_delete', 'create_time', 'update_time')
        read_only_fields = ('name', 'project')
        extra_kwargs = {
            'debugtalk': {
                'write_only': True
            }
        }