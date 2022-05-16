#!/usr/bin/env python
"""
-*- coding: utf-8 -*-
@Time    : 2022/5/16 14:36
@Author  : Chenzhida
@Email   : chenzhida3@163.com
@File    : run.py
@Describe:
@License : Copyright SideWalk Group © 2020~2022.All Rights Reserved
"""
from httprunner.api import HttpRunner
from httprunner.report import gen_html_report

runner = HttpRunner(log_level="INFO")
summary = runner.run('test.yaml')
# print(summary)
gen_html_report(summary=summary)