# -*- encoding: utf-8 -*-
'''
@File    : urls.py
@Time    : 2021/6/29 23:21
@Author  : Chenzd
@Software: PyCharm
'''
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from user import views


urlpatterns = [
    path('register/', views.RegisterView.as_view()),
    path('login/', obtain_jwt_token),
]