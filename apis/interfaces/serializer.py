# -*- encoding: utf-8 -*-
'''
@File    : serializer.py
@Time    : 2022/4/16 12:54
@Author  : Chenzd
@Software: PyCharm
接口序列器
'''
from rest_framework import serializers
from interfaces.models import Interfaces
from projects.models import Projects


class InterfaceSerializer(serializers.ModelSerializer):

    # 前端展示项目名，但实际保存到数据库是要用id
    project = serializers.StringRelatedField(help_text="项目名称")
    project_id = serializers.PrimaryKeyRelatedField(queryset=Projects.objects.all(), help_text="项目id")

    class Meta:
        model = Interfaces
        fields = ("id", "name", "tester", "project", "project_id", "desc", "create_time", "update_time")
        extra_kwargs = {
            'create_time': {
                'read_only': True
            },
            'update_time': {
                'read_only': True
            }
        }

    def create(self, validated_data):
        """新增接口"""
        project = validated_data.pop('project_id')
        validated_data['project'] = project
        interface = Interfaces.objects.create(**validated_data)
        return interface

    def update(self, instance, validated_data):
        """更新接口"""
        if 'project_id' in validated_data:
            project = validated_data.pop('project_id')
            validated_data['project'] = project
        return super().update(instance, validated_data)