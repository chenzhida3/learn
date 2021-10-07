# -*- encoding: utf-8 -*-
'''
@File    : time_format.py
@Time    : 2021/10/7 20:39
@Author  : Chenzd
@Software: PyCharm
格式化时间
'''
import re


def time_format(datas):
    datas_list = []
    for item in datas:
        # 格式化时间
        mtch = re.search(r'(.*)T(.*)\..*?', item['create_time'])
        item['create_time'] = mtch.group(1)+' '+mtch.group(2)
        mtch = re.search(r'(.*)T(.*)\..*?', item['update_time'])
        item['update_time'] = mtch.group(1) + ' ' + mtch.group(2)
        datas_list.append(item)

    return datas_list
