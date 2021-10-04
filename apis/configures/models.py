from django.db import models
from utils.base_models import BaseModel
# Create your models here.


class Configures(BaseModel):
    name = models.CharField(verbose_name='配置名称', help_text='配置名称', max_length=255, unique=True)
    author = models.CharField(verbose_name='作者', help_text='作者', max_length=255)
    request = models.TextField(verbose_name='请求', help_text='请求')
    interface = models.ForeignKey('interfaces.Interfaces', on_delete=models.CASCADE, verbose_name='所属接口',
                                  help_text='所属接口')

    class Meta:
        db_table = 'configures_tb'
        verbose_name = '配置表'
        verbose_name_plural = '配置表'

    def __str__(self):
        return self.name
