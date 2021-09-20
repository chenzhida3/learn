# -*- encoding: utf-8 -*-
'''
@File    : pagination.py
@Time    : 2021/9/20 16:53
@Author  : Chenzd
@Software: PyCharm
分页引擎定制
'''
from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class PageNumberPaginationManual(PageNumberPagination):
    page_size = 2  # 默认每页显示条数配置
    page_query_param = 'p'  # “页数”的请求参数名称, 默认是page
    page_size_query_param = 's'  # “分页大小”的请求参数名称

    # 觉得不适用, 那就拷贝出来,重载函数, 自己多加几个字段.
    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('page', self.page.number),
            ('total_page', self.page.paginator.num_pages),
            ('page_size', self.page.paginator.per_page),
            ('results', data)
        ]))
