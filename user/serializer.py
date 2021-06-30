# -*- encoding: utf-8 -*-
'''
@File    : serializer.py
@Time    : 2021/6/29 22:51
@Author  : Chenzd
@Software: PyCharm
'''
from rest_framework import serializers
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):
    '''注册接口的序列化器'''

    password_confirm = serializers.CharField(label='确认密码', min_length=6, max_length=20,
                                        help_text='确认密码', write_only=True,
                                        error_messages={'min_length': '最少要6个字符', 'max_length': '最大不超过20个字符'})
    token = serializers.CharField(label='token值', read_only=True, help_text='token值')

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'password_confirm', 'token')
        extra_kwargs = {
            'username': {
                'label': '用户名',
                'min_length': 6,
                'max_length': 20,
                'help_text': '用户名',
                'error_messages': {
                    'min_length': '最少要6个字符', 'max_length': '最大不超过20个字符'
                }
            },
            'password': {
                'label': '密码',
                'min_length': 6,
                'max_length': 20,
                'help_text': '密码',
                'write_only': True,
                'error_messages': {
                    'min_length': '最少要6个字符', 'max_length': '最大不超过20个字符'
                }
            },
            'email': {
                'label': '邮箱',
                'help_text': '邮箱',
                'required': True,
                'error_messages': {
                    'min_length': '最少要6个字符', 'max_length': '最大不超过20个字符'
                }
            }
        }

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        return super(RegisterSerializer, self).create(validated_data)