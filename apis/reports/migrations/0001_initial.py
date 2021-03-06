# Generated by Django 3.2.4 on 2021-10-02 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.AutoField(help_text='id主键', primary_key=True, serialize=False, verbose_name='id主键')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, help_text='逻辑删除', verbose_name='逻辑删除')),
                ('name', models.CharField(help_text='报告名称', max_length=255, unique=True, verbose_name='报告名称')),
                ('result', models.BooleanField(default=1, help_text='结果', verbose_name='结果')),
                ('count', models.IntegerField(help_text='用例总数', verbose_name='用例总数')),
                ('success', models.IntegerField(help_text='成功总数', verbose_name='成功总数')),
                ('html', models.TextField(blank=True, default='', help_text='内容', verbose_name='内容')),
                ('summary', models.TextField(blank=True, default='', help_text='报告详情', verbose_name='报告详情')),
            ],
            options={
                'verbose_name': '报告',
                'verbose_name_plural': '报告',
                'db_table': 'reports_tb',
            },
        ),
    ]
