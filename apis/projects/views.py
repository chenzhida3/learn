from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from projects.utils import get_count_by_project
from projects.serializer import *
from interfaces.models import Interfaces
# Create your views here.


class ProjectsViewSet(ModelViewSet):
    queryset = Projects.objects.filter(is_delete=False)
    serializer_class = ProjectModelSerializer
    permission_classes = (permissions.IsAuthenticated,)
    ordering_fields = ('id', 'name')
    filterset_fields = ['name', 'tester', 'leader', 'publish_app']

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
            datas = serializer.data
            datas = get_count_by_project(datas)
            return self.get_paginated_response(datas)

        serializer = self.get_serializer(queryset, many=True)
        datas = serializer.data
        datas = get_count_by_project(datas)
        return Response(datas)