from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView
from user.serializer import RegisterSerializer
from django.contrib.auth.models import User

class RegisterView(CreateAPIView):
    '''注册视图'''
    queryset = User.objects.all()
    serializer_class = RegisterSerializer



