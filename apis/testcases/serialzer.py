#!/usr/bin/env python
"""
-*- coding: utf-8 -*-
@Time    : 2022/5/23 15:47
@Author  : Chenzhida
@Email   : chenzhida3@163.com
@File    : serialzer.py
@Describe: 测试用例模块序列化器
@License : Copyright SideWalk Group © 2020~2022.All Rights Reserved
"""
from rest_framework import serializers
from configures.serialzer import InterfacesAnotherSerialzer
from testcases.models import TestCases


class TestcasesSerialzer(serializers.ModelSerializer):

    interface = InterfacesAnotherSerialzer(help_text='所属接口和项目信息')

    class Meta:

        model = TestCases
        fields = ('id', 'name', 'interface', 'include', 'author', 'request', 'create_time', 'update_time')
        extra_kwargs = {
            'create_time': {
                'read_only': True
            },
            'update_time': {
                'read_only': True
            },
            'request': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        '''
        创建用例
        '''
        if 'interface' in validated_data:
            interface_dict = validated_data.pop('interface')
            validated_data['interface_id'] = interface_dict['iid']
        return TestCases.objects.create(**validated_data)

    def update(self, instance, validated_data):
        '''
        更新用例
        '''
        if 'interface' in validated_data:
            interface_dict = validated_data.pop('interface')
            validated_data['interface_id'] = interface_dict['iid']
        return super().update(instance, validated_data)
