# -*- encoding: utf-8 -*-
'''
@File    : urls.py
@Time    : 2022/4/20 17:54
@Author  : Chenzd
@Software: PyCharm
'''
from testsuits import views
from rest_framework import routers

# 1.创建路由
router = routers.SimpleRouter()
# 2.注册路由
router.register(prefix='', viewset=views.TestsuitsViewSet)

urlpatterns = [

]
urlpatterns += router.urls