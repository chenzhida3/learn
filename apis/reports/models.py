from django.db import models
from utils.base_models import BaseModel
# Create your models here.

class Reports(BaseModel):
    """项目的数据库模型类"""

    name = models.CharField(verbose_name='报告名称', max_length=255, unique=True, help_text='报告名称')
    result = models.BooleanField(verbose_name='结果', default=1, help_text='结果')  # 1为成功，0为失败
    count = models.IntegerField(verbose_name='用例总数',  help_text='用例总数')
    success = models.IntegerField(verbose_name='成功总数', help_text='成功总数')
    html = models.TextField(verbose_name='内容', default='', blank=True, help_text='内容')
    summary = models.TextField(verbose_name='报告详情', help_text='报告详情', default='', blank=True)

    # 定义子类  用于设置当前数据模型的元数据信息
    class Meta:
        db_table = 'reports_tb'

        # 会在admin站点显示更人性化的表名
        verbose_name = '报告'
        verbose_name_plural = '报告'

    def __str__(self):
        return self.name
