# -*- encoding: utf-8 -*-
'''
@File    : serializer.py
@Time    : 2022/4/20 17:25
@Author  : Chenzd
@Software: PyCharm
序列化器
'''
from rest_framework import serializers
from testsuits.models import Testsuits
from projects.models import Projects


class TestSuitsSerializer(serializers.ModelSerializer):

    project = serializers.StringRelatedField(help_text='所属项目')
    project_id = serializers.PrimaryKeyRelatedField(queryset=Projects.objects.all(), help_text='项目id')

    class Meta:

        model = Testsuits
        exclude = ["is_delete"]
        extra_kwargs = {
            'create_time': {
                'read_only': True
            },
            'update_time': {
                'read_only': True
            }
        }

    def create(self, validated_data):
        project = validated_data.pop('project_id')
        validated_data['project'] = project
        testSuit = Testsuits.objects.create(**validated_data)
        return testSuit

    def update(self, instance, validated_data):
        """更新接口"""
        if 'project_id' in validated_data:
            project = validated_data.pop('project_id')
            validated_data['project'] = project
        return super().update(instance, validated_data)







