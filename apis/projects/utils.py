# -*- encoding: utf-8 -*-
'''
@File    : utils.py
@Time    : 2021/10/4 20:36
@Author  : Chenzd
@Software: PyCharm
项目工具类
'''
import re

from django.db.models import Count
from interfaces.models import Interfaces
from testsuits.models import Testsuits


def get_count_by_project(datas):
    datas_list = []
    for item in datas:
        project_id = item['id']
        interfaces_testcases_obj = Interfaces.objects.values('id').annotate(testcases=Count('testcases')).\
            filter(project_id=project_id, is_delete=False)
        interface_count = interfaces_testcases_obj.count()
        testcases_count = 0
        for one_dict in interfaces_testcases_obj:
            testcases_count += one_dict['testcases']
        interfaces_configures_obj = Interfaces.objects.values('id').annotate(configures=Count('configures')). \
            filter(project_id=project_id, is_delete=False)
        configures_count = 0
        for one_dict in interfaces_configures_obj:
            configures_count += one_dict['configures']
        testsuits_count = Testsuits.objects.filter(project_id=project_id, is_delete=False).count()

        item['interface_count'] = interface_count
        item['testcases_count'] = testcases_count
        item['configures_count'] = configures_count
        item['testsuits_count'] = testsuits_count
        datas_list.append(item)


    return datas_list
