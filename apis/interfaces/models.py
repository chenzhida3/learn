from django.db import models
from utils.base_models import BaseModel

# Create your models here.
class Interfaces(BaseModel):
    """接口的数据模型"""
    name = models.CharField(verbose_name='接口名称', max_length=255, unique=True, help_text='接口名称')
    tester = models.CharField(verbose_name='测试人员', max_length=50, help_text='测试人员')
    desc = models.TextField(verbose_name='简要描述', help_text='简要描述', blank=True, default='', null=True)

    # 更项目表是一对多关系  所以设置外键  on_delete指当projects表删除后，子表的project字段改如何处理
    # CASCADE--》子表该字段也会删除， SET_NULL--》子表该字段会设为空， PROJECT--》会报错  SET_DEFAULT--》会设置默认值
    project = models.ForeignKey('projects.Projects', on_delete=models.CASCADE, verbose_name='所属项目', help_text='所属项目')

    class Meta:
        db_table = 'interfaces_tb'
        verbose_name = '接口'
        verbose_name_plural = '接口'

    def __str__(self):
        return self.name