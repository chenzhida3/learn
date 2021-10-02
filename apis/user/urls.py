# -*- encoding: utf-8 -*-
'''
@File    : urls.py
@Time    : 2021/6/29 23:21
@Author  : Chenzd
@Software: PyCharm
'''
from django.urls import path, re_path
from rest_framework_jwt.views import obtain_jwt_token

from apis.user import views


urlpatterns = [
    path('register/', views.RegisterView.as_view()),
    path('login/', obtain_jwt_token),
    re_path(r'^(?P<username>\w{0,20})/count/$', views.UsernameView.as_view(),
            name='check_username'),
    path('email/', views.EmailValidateView.as_view(), name='check_email')
]