from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from envs.serializer import EnvsSerializer, EnvsNameSerializer
from rest_framework import permissions
from envs.models import Envs
from rest_framework.decorators import action
from utils.time_format import time_format
from utils.filter import envsFilter


class EnvsViewSet(ModelViewSet):
    queryset = Envs.objects.filter(is_delete=False).order_by('id')
    permission_classes = (permissions.AllowAny,)
    serializer_class = EnvsSerializer
    ordering_fields = ('id', 'name')
    filterset_class = envsFilter

    def perform_destroy(self, instance):
        instance.is_delete = True
        instance.save()

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

    @action(methods=['get'], detail=False)
    def names(self, request, pk=None):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == 'names':
            return EnvsNameSerializer
        else:
            return EnvsSerializer