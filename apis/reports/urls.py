# -*- encoding: utf-8 -*-
'''
@File    : urls.py
@Time    : 2021/6/29 23:21
@Author  : Chenzd
@Software: PyCharm
'''
from django.urls import path, include

from reports import views
from rest_framework import routers

# 1.创建路由
router = routers.SimpleRouter()
# 2.注册路由
router.register(prefix='', viewset=views.ReportViewSet)

urlpatterns = [

]
urlpatterns += router.urls
