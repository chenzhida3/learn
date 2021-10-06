# -*- encoding: utf-8 -*-
'''
@File    : serializer.py
@Time    : 2021/9/19 16:35
@Author  : Chenzd
@Software: PyCharm
序列化器
'''
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator
from projects.models import Projects
from debugtalks.models import Debugtalks

# 自定义校验器
def str_length_unique(name):
    if len(name) < 3:
        raise serializers.ValidationError("字符长度至少要大于3")
    return name

class ProjectModelSerializer(ModelSerializer):
    name = serializers.CharField(label='项目名称', max_length=255, min_length=3, help_text='项目名称',
                                 validators=[UniqueValidator(queryset=Projects.objects.all(),
                                                             message='项目名称不能重复'),
                                             str_length_unique],
                                 error_messages={"max_length": "长度不能超过255个字节",
                                                 "min_length": "长度不能少于3个字符"})

    class Meta:
        # 指定参考哪一个模型类来创建
        model = Projects
        # 2.指定为模型类的哪些字段，来生成序列化器
        # fields = "__all__"
        # 除了元祖里面的字段 其它全部生成序列化字段
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
        project_obj = super().create(validated_data)
        Debugtalks.objects.create(project=project_obj)
        return project_obj

    # 单字段校验  validate_要校验的字段名
    def validate_name(self, value):
        if not value.endswith('项目'):
            raise serializers.ValidationError('项目名称必须以"项目"结尾')
        return value  # 校验后要返回   不然就返回None

    # 多字段校验 validate
    def validate(self, attrs):
        pass
        return attrs


class ProjectsNameSerializer(ModelSerializer):

    class Meta:
        model = Projects
        fields = ('id', 'name')


class InterfaceNameSerializer(ModelSerializer):

    class Meta:
        model = Projects
        fields = ('id', 'name', 'tester')


class InterfacesByProjectIdSerializer(ModelSerializer):
    interfaces_set = InterfaceNameSerializer(read_only=True, many=True)

    class Meta:
        model = Projects
        fields = ('id', 'interfaces_set')






