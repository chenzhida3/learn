# 自定义字段过滤器  使其支持模糊查询

from django_filters.rest_framework import FilterSet
import django_filters
from testsuits.models import Testsuits
from projects.models import Projects
from interfaces.models import Interfaces
from envs.models import Envs
from configures.models import Configures

# exact表示精确匹配, 并且忽略大小写
# icontains表示模糊查询（包含），并且忽略大小写
# (look_expr='exact')  # exact表示精确匹配
#  lookup_expr='gte',help_text="年龄大等于"
#  age_l = filters.NumberFilter(field_name='age', lookup_expr='lte',help_text="年龄小等于")


class testsuitsFilter(FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')  # icontains，包含且忽略大小写
    id = django_filters.CharFilter(field_name='id', lookup_expr='exact')

    class Meta:
        # 指定模型
        models = Testsuits
        # 指定需要模糊查询的字段
        fields = ['id', 'name']


class projectsFilter(FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')  # icontains，包含且忽略大小写
    id = django_filters.CharFilter(field_name='id', lookup_expr='exact')
    tester = django_filters.CharFilter(field_name='tester', lookup_expr='icontains')  # icontains，包含且忽略大小写
    leader = django_filters.CharFilter(field_name='leader', lookup_expr='icontains')  # icontains，包含且忽略大小写
    publish_app = django_filters.CharFilter(field_name='publish_app', lookup_expr='icontains')  # icontains，包含且忽略大小写

    class Meta:
        # 指定模型
        models = Projects
        # 指定需要模糊查询的字段
        fields = ['id', 'name', 'tester', 'leader', 'publish_app']


class interfacesFilter(FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')  # icontains，包含且忽略大小写
    id = django_filters.CharFilter(field_name='id', lookup_expr='exact')
    tester = django_filters.CharFilter(field_name='tester', lookup_expr='icontains')  # icontains，包含且忽略大小写

    class Meta:
        # 指定模型
        models = Interfaces
        # 指定需要模糊查询的字段
        fields = ['id', 'name', 'tester']


class envsFilter(FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')  # icontains，包含且忽略大小写
    id = django_filters.CharFilter(field_name='id', lookup_expr='exact')
    base_url = django_filters.CharFilter(field_name='base_url', lookup_expr='icontains')  # icontains，包含且忽略大小写

    class Meta:
        # 指定模型
        models = Envs
        # 指定需要模糊查询的字段
        fields = ['id', 'name', 'base_url']


class configureFilter(FilterSet):
    id = django_filters.CharFilter(field_name='id', lookup_expr='exact')
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    author = django_filters.CharFilter(field_name='author', lookup_expr='icontains')

    class Meta:
        # 指定模型
        models = Configures
        # 指定需要模糊查询的字段
        fields = ['id', 'name', 'author']