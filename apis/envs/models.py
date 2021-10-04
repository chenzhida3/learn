from django.db import models
from utils.base_models import BaseModel
# Create your models here.


class Envs(BaseModel):
    name = models.CharField(verbose_name='环境名称', help_text='环境名称', max_length=255, unique=True)
    base_url = models.URLField(verbose_name='基础路由', help_text='基础路由', max_length=200)
    desc = models.TextField(verbose_name='描述', help_text='描述', blank=True, default='', null=True)

    class Meta:
        db_table = 'envs_tb'
        verbose_name = '环境'
        verbose_name_plural = '环境'

    def __str__(self):
        return self.name
