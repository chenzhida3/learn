# -*- encoding: utf-8 -*-
'''
@File    : serializer.py
@Time    : 2022/4/18 20:44
@Author  : Chenzd
@Software: PyCharm
环境模块序列化器
'''
from rest_framework import serializers
from envs.models import Envs


class EnvsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Envs
        fields = ('id', 'name', 'base_url', 'create_time', 'update_time')

        extra_kwargs = {
            'create_time': {
                'read_only': True
            },
            'update_time': {
                'read_only': True
            }
        }


class EnvsNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Envs
        fields = ('id', 'name')
