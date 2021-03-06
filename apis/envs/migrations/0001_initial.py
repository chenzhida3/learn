# Generated by Django 3.2.4 on 2021-10-02 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Envs',
            fields=[
                ('id', models.AutoField(help_text='id主键', primary_key=True, serialize=False, verbose_name='id主键')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, help_text='逻辑删除', verbose_name='逻辑删除')),
                ('name', models.CharField(help_text='环境名称', max_length=255, unique=True, verbose_name='环境名称')),
                ('base_url', models.URLField(help_text='基础路由', verbose_name='基础路由')),
                ('desc', models.TextField(blank=True, default='', help_text='描述', null=True, verbose_name='描述')),
            ],
            options={
                'verbose_name': '环境',
                'verbose_name_plural': '环境',
                'db_table': 'envs_tb',
            },
        ),
    ]
