from django.db import models
from utils.base_models import BaseModel
# Create your models here.


class Testsuits(BaseModel):
    name = models.CharField(verbose_name='内置函数名', help_text='内置函数名', max_length=255, unique=True)
    include = models.TextField(verbose_name='包含接口', help_text='包含接口', null=True)
    request = models.TextField(verbose_name='请求', help_text='请求')
    project = models.ForeignKey('projects.Projects', on_delete=models.CASCADE, verbose_name='所属项目',
                                  help_text='所属项目')

    class Meta:
        db_table = 'testsuits_tb'
        verbose_name = '用例步骤'
        verbose_name_plural = '用例步骤'

    def __str__(self):
        return self.name
