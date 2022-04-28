from django.db import models
from utils.base_models import BaseModel
# Create your models here.


class Testsuits(BaseModel):
    name = models.CharField(verbose_name='套件名', help_text='套件名', max_length=255, unique=True)
    include = models.TextField(verbose_name='包含接口', help_text='包含接口', null=True)
    project = models.ForeignKey('projects.Projects', on_delete=models.CASCADE, verbose_name='所属项目',
                                  help_text='所属项目')
    desc = models.TextField(verbose_name='简要描述', help_text='简要描述', blank=True, default='', null=True)

    class Meta:
        db_table = 'testsuits_tb'
        verbose_name = '测试套件'
        verbose_name_plural = '测试套件'

    def __str__(self):
        return self.name
