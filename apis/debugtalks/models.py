from django.db import models
from utils.base_models import BaseModel
# Create your models here.


class Debugtalks(BaseModel):
    name = models.CharField(verbose_name='内置函数名', help_text='内置函数名', max_length=255, default='debugtalk.py')
    debugtalk = models.TextField(verbose_name='debugtalk.py文件', help_text='debugtalk.py文件', default='#debugtalk.py')
    project = models.OneToOneField('projects.Projects', on_delete=models.CASCADE, verbose_name='所属项目',
                                  help_text='所属项目')

    class Meta:
        db_table = 'debugtalks_tb'
        verbose_name = '内置函数表'
        verbose_name_plural = '内置函数表'

    def __str__(self):
        return self.name
