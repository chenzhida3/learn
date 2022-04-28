from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from testsuits.serializer import TestSuitsSerializer
from rest_framework import permissions
from testsuits.models import Testsuits
from utils.time_format import time_format


class TestsuitsViewSet(ModelViewSet):

    serializer_class = TestSuitsSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = Testsuits.objects.filter(is_delete=False).order_by('id')
    ordering_fields = ('id', 'name')
    filterset_fields = ['id', 'name']

    def perform_destroy(self, instance):
        """逻辑删除"""
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