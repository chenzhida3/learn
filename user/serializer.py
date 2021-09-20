# -*- encoding: utf-8 -*-
'''
@File    : serializer.py
@Time    : 2021/6/29 22:51
@Author  : Chenzd
@Software: PyCharm
'''
import logging
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_jwt.settings import api_settings
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
                'write_only': True,
                'required': True,
                'validators': [UniqueValidator(queryset=User.objects.all(), message='该邮箱已被注册')],
                'error_messages': {
                    'min_length': '最少要6个字符', 'max_length': '最大不超过20个字符'
                }
            }
        }

    # 重写validate校验两次密码是否输入一致
    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.get('password_confirm')
        if password != password_confirm:
            logging.error('两次输入密码不一致', password, password_confirm)
            raise serializers.ValidationError('两次输入密码不一致!')
        return attrs

    def create(self, validated_data):
        del validated_data['password_confirm']
        user = User.objects.create_user(**validated_data)

        # 生成token并在序列化器输出
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        user.token = token
        return user
