# -*- encoding: utf-8 -*-
'''
@File    : serializer.py
@Time    : 2021/9/19 16:35
@Author  : Chenzd
@Software: PyCharm
序列化器
'''
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from projects.models import Projects

# 自定义校验器
def str_length_unique(name):
    if len(name) < 3:
        raise serializers.ValidationError("字符长度至少要大于3")
    return name

class ProjectSerializer(serializers.Serializer):
    """
    创建项目序列化器类
    """
    id = serializers.IntegerField(label='ID', read_only=True)
    name = serializers.CharField(label='项目名称', max_length=255, help_text='项目名称',
                                 validators=[UniqueValidator(queryset=Projects.objects.all(),
                                                             message='项目名称不能重复'),
                                             str_length_unique])
    leader = serializers.CharField(label='负责人', max_length=50, help_text='负责人')
    tester = serializers.CharField(label='测试人员', max_length=50, help_text='测试人员')
    programer = serializers.CharField(label='开发人员', max_length=50, help_text='开发人员')
    publish_app = serializers.CharField(label='发布应用', max_length=200, help_text='发布应用')
    # null设置数据库中此字段允许为空   blank设置前端可以不传值   default设置默认值
    desc = serializers.CharField(label='简要描述', help_text='简要描述', allow_blank=True, default='', allow_null=True)

    # 单字段校验  validate_要校验的字段名
    def validate_name(self, value):
        if not value.endswith('项目'):
            raise serializers.ValidationError('项目名称必须以"项目"结尾')
        return value  # 校验后要返回   不然就返回None

    # 多字段校验 validate
    def validate(self, attrs):
        pass
        return attrs

    # 数据库 创建数据
    def create(self, validated_data):
        return Projects.objects.create(**validated_data)

    # 数据库 更新数据
    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.leader = validated_data['leader']
        instance.tester = validated_data['tester']
        instance.programer = validated_data['programer']
        instance.publish_app = validated_data['publish_app']
        instance.desc = validated_data['desc']
        instance.save()
        return instance



