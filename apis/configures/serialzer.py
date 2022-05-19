#!/usr/bin/env python
"""
-*- coding: utf-8 -*-
@Time    : 2022/5/16 15:47
@Author  : Chenzhida
@Email   : chenzhida3@163.com
@File    : serialzer.py
@Describe: 配置模块序列化器
@License : Copyright SideWalk Group © 2020~2022.All Rights Reserved
"""
from rest_framework import serializers
from configures.models import Configures
from interfaces.models import Interfaces
from projects.models import Projects
from utils.validates import whether_existed_project_id, whether_existed_interface_id


class InterfacesAnotherSerialzer(serializers.ModelSerializer):
    project = serializers.StringRelatedField(help_text='项目名称')
    pid = serializers.IntegerField(validators=[whether_existed_project_id], help_text='项目id', write_only=True)
    iid = serializers.IntegerField(validators=[whether_existed_interface_id], write_only=True, help_text='接口id')

    class Meta:
        model = Interfaces
        fields = ('iid', 'name', 'project', 'pid')
        extra_kwargs = {
            'iid': {
                'write_only': True
            },
            'name': {
                'read_only': True
            }
        }

    def validate(self, attrs):
        '''
        检查项目id于接口id是否一致
        '''
        if not Interfaces.objects.filter(is_delete=False, id=attrs['iid'], project_id=attrs['pid']).exists():
            raise serializers.ValidationError("项目和接口信息不对应！")
        return attrs


class ConfiguresSerialzer(serializers.ModelSerializer):
    interface = InterfacesAnotherSerialzer(help_text='项目id和接口id')

    class Meta:

        model = Configures
        fields = ('id', 'name', 'interface', 'author', 'request', 'create_time', 'update_time')
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
        创建配置
        '''
        if 'interface' in validated_data:
            interface_dict = validated_data.pop('interface')
            validated_data['interface_id'] = interface_dict['iid']
        return Configures.objects.create(**validated_data)

    def update(self, instance, validated_data):
        '''
        更新配置
        '''
        if 'interface' in validated_data:
            interface_dict = validated_data.pop('interface')
            validated_data['interface_id'] = interface_dict['iid']
        return super().update(instance, validated_data)
