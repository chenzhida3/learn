# -*- encoding: utf-8 -*-
'''
@File    : urls.py
@Time    : 2021/6/29 23:21
@Author  : Chenzd
@Software: PyCharm
'''
from django.urls import path

from projects import views


urlpatterns = [
    path('a/', views.ProjectsView.as_view()),
    # path('login/', obtain_jwt_token),
]