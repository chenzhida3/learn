from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from utils.time_format import time_format
from projects.utils import get_count_by_project
from projects.serializer import *
from interfaces.models import Interfaces
from utils.filter import projectsFilter


# Create your views here.


class ProjectsViewSet(ModelViewSet):
    queryset = Projects.objects.filter(is_delete=False).order_by('id')
    serializer_class = ProjectModelSerializer
    # 权限
    permission_classes = (permissions.AllowAny,)
    ordering_fields = ('id', 'name')
    filterset_class = projectsFilter

    def perform_destroy(self, instance):
        instance.is_delete = True
        instance.save()

    @action(methods=['get'], detail=False)
    def names(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ProjectsNameSerializer(instance=queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True)
    def interfaces(self, request, pk=None):
        interface_objs = Interfaces.objects.filter(project__id=pk, is_delete=False)
        one_list = []
        for obj in interface_objs:
            one_list.append({
                'id': obj.id,
                'name': obj.name
            })
        return Response(data=one_list)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            datas = time_format(serializer.data)
            datas = get_count_by_project(datas)
            return self.get_paginated_response(datas)

        serializer = self.get_serializer(queryset, many=True)
        datas = time_format(serializer.data)
        datas = get_count_by_project(datas)
        return Response(datas)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        datas = []
        datas.append(serializer.data)
        datas_list = time_format(datas)
        return Response(datas_list)

    # 重写部分更新接口
    def partial_update(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            project_obj = Projects.objects.get(is_delete=False, pk=pk)
        except:
            return Response(data={'pk': 'id值为空'}, status=400)
        serializer = ProjectModelSerializer(instance=project_obj, data=request.data, partial=True,
                                            context={'request': request})
        serializer.is_valid(raise_exception=True)
        book_obj = serializer.save()
        return Response(ProjectModelSerializer(book_obj).data)

    # 重写更新接口
    def update(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            try:
                project_obj = Projects.objects.get(is_delete=False, pk=pk)
            except:
                return Response(data={'pk': 'id值为空'}, status=400)
            serializer = ProjectModelSerializer(instance=project_obj, data=request.data, partial=False,
                                                context={'request': request})
            serializer.is_valid(raise_exception=True)
            book_obj = serializer.save()
            return Response(ProjectModelSerializer(book_obj).data)
