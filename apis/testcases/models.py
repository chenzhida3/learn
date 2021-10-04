from django.db import models
from utils.base_models import BaseModel
# Create your models here.


class TestCases(BaseModel):
    name = models.CharField(verbose_name='用例名称', help_text='用例名称', max_length=255, unique=True)
    include = models.TextField(verbose_name='前置', help_text='用例执行的前置顺序', null=True)
    author = models.CharField(verbose_name='作者', help_text='作者', max_length=255)
    request = models.TextField(verbose_name='请求', help_text='请求')
    interface = models.ForeignKey('interfaces.Interfaces', on_delete=models.CASCADE, verbose_name='所属接口', help_text='所属接口')

    class Meta:
        db_table = 'testcases_tb'
        verbose_name = '用例'
        verbose_name_plural = '用例'

    def __str__(self):
        return self.name
