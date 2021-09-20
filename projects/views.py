import json

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status

from rest_framework.response import Response
from projects.models import Projects
from projects.serializer import ProjectModelSerializer
from rest_framework.generics import GenericAPIView
# Create your views here.
class ProjectsList(GenericAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectModelSerializer

    ordering_fields = ['name']
    filterset_fields = ['name', 'tester', 'leader']
    # 获取所有项目
    def get(self, request):
        project_qs = self.get_queryset()
        project_qs = self.filter_queryset(project_qs)  # 过滤
        page = self.paginate_queryset(project_qs)
        if page is not None:
            serializer = self.get_serializer(instance=page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(instance=project_qs, many=True)
        return Response(serializer.data)

    # 创建
    def post(self, request):
        """新增项目"""
        json_data = request.body.decode('utf-8')
        python_data = json.loads(json_data, encoding='utf-8')

        serializer = self.get_serializer(data=python_data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return Response(serializer.errors)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

class ProjectsDetail(GenericAPIView):
    """项目详情"""
    # def get_object(self, pk):
    #     try:
    #         return Projects.objects.get(id=pk)
    #     except Projects.DoesNotExist:
    #         raise Http404
    queryset = Projects.objects.all()
    serializer_class = ProjectModelSerializer

    # 获取单个详情
    def get(self, request, pk):
        """获取项目详情"""
        # 1、校验pk  省略
        project = self.get_object()
        # serializer = ProjectModelSerializer(instance=project)
        serializer = self.get_serializer(isinstance=project)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 更新
    def put(self, request, pk):
        project = self.get_object()
        # 从前端获取json数据，转化成python的类型
        json_data = request.body.decode('utf-8')
        python_data = json.loads(json_data, encoding='utf-8')

        serializer = self.get_serializer(instance=project, data=python_data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return Response(serializer.errors, status.HTTP_404_NOT_FOUND)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

    # 删除
    def delete(self, request, pk):
        project = self.get_object()
        project.delete()
        return Response(None, status.HTTP_204_NO_CONTENT)