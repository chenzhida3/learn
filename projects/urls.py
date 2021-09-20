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
    path('', views.ProjectsList.as_view()),
    path('<int:pk>/', views.ProjectsDetail.as_view()),
]