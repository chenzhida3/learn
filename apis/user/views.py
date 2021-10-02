from django.shortcuts import render

# Create your views here.

from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from apis.user.serializer import RegisterSerializer
from django.contrib.auth.models import User

class RegisterView(CreateAPIView):
    '''注册视图'''
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class UsernameView(APIView):
    """用户名校验"""
    def get(self, request, username):
        one_dict = {
            "name": username,
            "count": User.objects.filter(username=username).count()
        }
        return Response(one_dict)


class EmailValidateView(APIView):
    """校验邮箱是否存在"""
    def get(self, request):
        email = request.GET.get('email')
        data_dict = {
            "email": email,
            "count": User.objects.filter(email=email).count()
        }
        return Response(data_dict)



