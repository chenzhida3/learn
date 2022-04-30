from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from configures.models import Configures
from interfaces.serializer import *
from testcases.models import TestCases
from utils.time_format import time_format
from interfaces.utils import get_count_by_interface
from rest_framework.decorators import action
from utils.filter import interfacesFilter


class InterfaceViewSet(ModelViewSet):
    queryset = Interfaces.objects.filter(is_delete=False).order_by('id')
    serializer_class = InterfaceSerializer
    permission_classes = (permissions.AllowAny,)
    ordering_fields = ('id', 'name')
    filterset_class = interfacesFilter

    def perform_destroy(self, instance):
        """逻辑删除"""
        instance.is_delete = True
        instance.save()

    """重写list  将时间格式化"""

    def list(self, request, *args, **kwargs):
        # request.META["CSRF_COOKIE_USED"] = True
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            datas = time_format(serializer.data)
            datas = get_count_by_interface(datas)
            return self.get_paginated_response(datas)

        serializer = self.get_serializer(queryset, many=True)
        datas = time_format(serializer.data)
        datas = get_count_by_interface(datas)
        return Response(datas)

    @action(methods=['get'], detail=True)
    def testcases(self, request, pk=None):
        testcase_obj = TestCases.objects.filter(interface_id=pk, is_delete=False)
        one_list = []
        for obj in testcase_obj:
            one_list.append({
                'id': obj.id,
                'name': obj.name
            })
        return Response(data=one_list)

    @action(methods=['get'], detail=True, url_path='configs')
    def configs(self, request, pk=None):
        configs_obj = Configures.objects.filter(interface_id=pk, is_delete=False)
        one_list = []
        for obj in configs_obj:
            one_list.append({
                'id': obj.id,
                'name': obj.name
            })
        return Response(data=one_list)