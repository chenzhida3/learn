from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView
from user.serializer import RegisterSerializer


class RegisterView(CreateAPIView):
    '''注册视图'''
    serializer_class = RegisterSerializer
