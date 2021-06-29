# -*- encoding: utf-8 -*-
'''
@File    : urls.py
@Time    : 2021/6/29 23:21
@Author  : Chenzd
@Software: PyCharm
'''
from django.urls import path
from user import views


urlpatterns = [
    path('register/', views.RegisterView.as_view()),
]