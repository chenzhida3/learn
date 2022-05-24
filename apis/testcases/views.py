from django.shortcuts import render

# Create your views here.
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from interfaces.models import Interfaces
from testcases.models import TestCases
from testcases.serialzer import TestcasesSerialzer
from utils.filter import testcasesFilter
import json
from utils import handle_datas
from utils.time_format import time_format


class TestcasesViewSet(ModelViewSet):
    queryset = TestCases.objects.filter(is_delete=False).order_by('id')
    serializer_class = TestcasesSerialzer
    permission_classes = (permissions.AllowAny,)
    ordering_fields = ('id', 'name')
    filterset_class = testcasesFilter

    def perform_destroy(self, instance):
        '''
        逻辑删除
        '''
        instance.is_delete = True
        instance.save()

    @action(methods=['get'], detail=True)
    def interfaces(self, request, pk=None):
        testcase_objs = TestCases.objects.filter(interface__id=pk, is_delete=False)
        datas = []
        for testcase in testcase_objs:
            one_list = {
                'id': testcase.id,
                'name': testcase.name,
            }
            datas.append(one_list)
        return Response(data=datas)

    def retrieve(self, request, *args, **kwargs):
        """
        重写获取详情接口
        """
        testcase_obj = self.get_object()

        # 用例前置信息
        testcase_include = json.loads(testcase_obj.include)

        # 用例请求信息
        testcase_request = json.loads(testcase_obj.request)
        testcase_request_datas = testcase_request.get("test").get("request")

        # 用例的预期结果
        testcase_validate = testcase_request.get("test").get("validate")
        testcase_validate_list = handle_datas.handle_data1(testcase_validate)

        # 用例的参数
        testcase_params = testcase_request.get("test").get("params")
        testcase_params_list = handle_datas.handle_data4(testcase_params)

        # 用例的请求头
        testcase_headers = testcase_request_datas.get("headers")
        testcase_headers_list = handle_datas.handle_data4(testcase_headers)

        # 用例的变量列表
        testcase_variables = testcase_request.get("test").get("variables")
        testcase_variables_list = handle_datas.handle_data2(testcase_variables)

        # 处理from表单
        testcase_form_datas = testcase_request_datas.get("data")
        testcase_form_datas_list = handle_datas.handle_data6(testcase_form_datas)

        # 处理json数据
        testcase_json_datas = json.dumps(testcase_request_datas.get("json"), ensure_ascii=False)

        # 处理extract数据 （导出）
        testcase_extract_datas = testcase_request.get("test").get("extract")
        testcase_extract_datas_list = handle_datas.handle_data3(testcase_extract_datas)

        # 处理parameters数据（参数化）
        testcase_parameters_datas = testcase_request.get("test").get("parameters")
        testcase_parameters_datas_list = handle_datas.handle_data3(testcase_parameters_datas)

        # 处理setupHooks数据
        testcase_setup_hooks_datas = testcase_request.get("test").get("setup_hooks")
        testcase_setup_hooks_datas_list = handle_datas.handle_data5(testcase_setup_hooks_datas)

        # 处理teardownHooks数据
        testcase_tear_down_datas = testcase_request.get("test").get("teardown_hooks")
        testcase_tear_down_datas_list = handle_datas.handle_data5(testcase_tear_down_datas)

        selected_interface_id = testcase_obj.interface_id
        selected_project_id = Interfaces.objects.get(id=selected_interface_id).project_id
        selected_configure_id = testcase_include.get('config')
        selected_testcase_id = testcase_include.get('testcases')

        datas = {
            'author': testcase_obj.author,
            'config_name': testcase_obj.name,
            'selected_interface_id': selected_interface_id,
            'selected_project_id': selected_project_id,
            'selected_configure_id': selected_configure_id,
            'selected_testcase_id': selected_testcase_id,

            'method': testcase_request_datas.get('method'),
            'url': testcase_request_datas.get('url'),
            'param': testcase_params_list,
            'header': testcase_headers_list,
            'variable': testcase_form_datas_list,
            'jsonVariable': testcase_json_datas,

            'extrat': testcase_extract_datas_list,
            'validate': testcase_validate_list,
            'globaVar': testcase_variables_list,
            'parameterized': testcase_parameters_datas_list,
            'setupHooks': testcase_setup_hooks_datas_list,
            'teardownHooks': testcase_tear_down_datas_list

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

    # 重写部分更新接口
    def partial_update(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            testcases_obj = TestCases.objects.get(is_delete=False, pk=pk)
        except:
            return Response(data={'pk': 'id值为空'}, status=400)

        serializer = TestcasesSerialzer(instance=testcases_obj, data=request.data, partial=True,
                                         context={'request': request})
        serializer.is_valid(raise_exception=True)
        book_obj = serializer.save()
        return Response(TestcasesSerialzer(book_obj).data)