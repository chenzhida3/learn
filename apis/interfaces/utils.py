# -*- encoding: utf-8 -*-
'''
@File    : utils.py
@Time    : 2022/4/16 13:47
@Author  : Chenzd
@Software: PyCharm
'''
from django.db.models import Count
from interfaces.models import Interfaces


def get_count_by_interface(datas):
    datas_list = []
    for item in datas:
        interface_id = item['id']
        # 计算用例数
        interfaces_testcases_obj = Interfaces.objects.values('id').annotate(testcases=Count('testcases')). \
            filter(id=interface_id, is_delete=False)

        testcases_count = 0
        for one_dict in interfaces_testcases_obj:
            testcases_count += one_dict['testcases']

        # 计算配置数
        interfaces_configures_obj = Interfaces.objects.values('id').annotate(configures=Count('configures')). \
            filter(id=interface_id, is_delete=False)
        configures_count = 0
        for one_dict in interfaces_configures_obj:
            configures_count += one_dict['configures']

        item['testcases_count'] = testcases_count
        item['configures_count'] = configures_count

        datas_list.append(item)

    return datas_list
