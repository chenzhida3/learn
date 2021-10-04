from django.db import models
from utils.base_models import BaseModel
# Create your models here.

class Projects(BaseModel):
    """项目的数据库模型类"""

    # verbose_name用于设置字段名    unique用于设置当前字段是否唯一
    # help_test 用于api文档中的一个中文名
    name = models.CharField(verbose_name='项目名称', max_length=255, unique=True, help_text='项目名称')
    leader = models.CharField(verbose_name='负责人', max_length=50, help_text='负责人')
    tester = models.CharField(verbose_name='测试人员', max_length=50, help_text='测试人员')
    programer = models.CharField(verbose_name='开发人员', max_length=50, help_text='开发人员')
    publish_app = models.CharField(verbose_name='发布应用', max_length=200, help_text='发布应用')
    # null设置数据库中此字段允许为空   blank设置前端可以不传值   default设置默认值
    desc = models.TextField(verbose_name='简要描述', help_text='简要描述', blank=True, default='', null=True)

    # 定义子类  用于设置当前数据模型的元数据信息
    class Meta:
        db_table = 'projects_tb'

        # 会在admin站点显示更人性化的表名
        verbose_name = '项目'
        verbose_name_plural = '项目'
        ordering = ['id']  # 分页查询需要这个字段，不然会有警告

    def __str__(self):
        return self.name
