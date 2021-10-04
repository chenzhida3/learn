# -*- encoding: utf-8 -*-
'''
@File    : base_models.py
@Time    : 2021/10/2 15:48
@Author  : Chenzd
@Software: PyCharm
'''

from django.db import models


class BaseModel(models.Model):
    id = models.AutoField(verbose_name='id主键', primary_key=True, help_text='id主键')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', help_text='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间', help_text='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除', help_text='逻辑删除')

    class Meta:
        # 为抽象模型类，用于其他模型来继承，迁移时不会创建Basemodel表来
        abstract = True
        verbose_name = '公共字段表'
        db_table = 'BaseModel'
