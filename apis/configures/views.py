from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from configures.models import Configures
from configures.serialzer import ConfiguresSerialzer
from rest_framework import permissions
import json
from utils import handle_datas
from interfaces.models import Interfaces
from rest_framework.response import Response
from utils.filter import configureFilter
from utils.time_format import time_format


class ConfiguresViewSet(ModelViewSet):
    queryset = Configures.objects.filter(is_delete=False).order_by('id')
    serializer_class = ConfiguresSerialzer
    permission_classes = (permissions.AllowAny,)
    ordering_fields = ('id', 'name')
    filterset_class = configureFilter

    def perform_destroy(self, instance):
        '''
        逻辑删除
        '''
        instance.is_delete = True
        instance.save()

    def retrieve(self, request, *args, **kwargs):
        """获取配置详情"""
        config_obj = self.get_object()
        config_request = json.loads(config_obj.request)

        # 处理全局变量数据
        config_variables = config_request['config'].get('variables')
        config_variables_list = handle_datas.handle_data2(config_variables)

        # 处理配置文件名称
        config_name = config_request['config']['name']

        # 处理基础路由
        config_baseUrl = config_request['config']['base_url']

        selected_interface_id = config_obj.interface_id
        selected_project_id = Interfaces.objects.get(id=selected_interface_id).project_id
        datas = {
            'author': config_obj.author,
            'config_name': config_name,
            'base_url': config_baseUrl,
            'selected_interface_id': selected_interface_id,
            'selected_project_id': selected_project_id,
            'globalVar': config_variables_list
        }
        return Response(datas)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            datas = time_format(serializer.data)
            return self.get_paginated_response(datas)

        serializer = self.get_serializer(queryset, many=True)
        datas = time_format(serializer.data)
        return Response(datas)