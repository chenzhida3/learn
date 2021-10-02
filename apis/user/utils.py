# -*- encoding: utf-8 -*-
'''
@File    : utils.py
@Time    : 2021/6/30 22:29
@Author  : Chenzd
@Software: PyCharm
'''


def jwt_response_payload_handler(token, user=None, request=None):
    """自定义jwt认证成功返回数据"""
    return {
        'token': token,
        'userId': user.id,
        'username': user.username
    }
