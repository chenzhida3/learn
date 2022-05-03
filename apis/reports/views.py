import json
from datetime import datetime
import os

from django.utils.encoding import escape_uri_path
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from django.http import StreamingHttpResponse, HttpResponse
from rest_framework import permissions
from .serializer import ReportSerializer
from .models import Reports
from utils.time_format import time_format
from .utils import result_format, get_file_content
import re
from learn import settings
# Create your views here.


class ReportViewSet(ModelViewSet):

    queryset = Reports.objects.filter(is_delete=False).order_by('id')
    serializer_class = ReportSerializer
    # 权限
    permission_classes = (permissions.AllowAny,)
    ordering_fields = ('id', 'name')

    def perform_destroy(self, instance):
        instance.is_delete = True
        instance.save()

    def list(self, request, *args, **kwargs):

        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            datas = time_format(serializer.data)
            datas = result_format(datas)
            return self.get_paginated_response(datas)

        serializer = self.get_serializer(queryset, many=True)
        datas = time_format(serializer.data)
        datas = result_format(datas)
        return Response(datas)

    @action(detail=True)
    def download(self, request, pk=None):
        instance = self.get_object()
        html = instance.html
        name = instance.name
        mtch = re.match(r'(.*_)\d+', name)
        if mtch:
            # 取出分组
            mtch = mtch.group(1)
            file_name = mtch + datetime.strftime(datetime.now(), '%Y%m%d%H%M%S') + '.html'
        else:
            file_name = name

        report_path = os.path.join(settings.REPORTS_DIR, file_name)
        # 写入html
        with open(report_path, 'w+', encoding='utf-8') as f:
            f.write(html)
        response = StreamingHttpResponse(get_file_content(report_path))

        # 为了文件名能显示中文
        report_path_final = escape_uri_path(file_name)

        response['Content-Type'] = "application/octet-stream"
        response['Content-Disposition'] = "attachment; filename*=UTF-8''{}".format(report_path_final)
        return response

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        datas = serializer.data
        try:
            datas['summary'] = json.loads(datas['summary'], encodings='utf-8')
        except Exception as e:
            pass
        return Response(datas)