from django.shortcuts import render

# Create your views here.
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from testsuits.serializer import TestSuitsSerializer
from rest_framework import permissions
from testsuits.models import Testsuits
from utils.time_format import time_format


class TestsuitsViewSet(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.DestroyModelMixin,
                       GenericViewSet):

    serializer_class = TestSuitsSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = Testsuits.objects.filter(is_delete=False).order_by('id')
    ordering_fields = ('id', 'name')

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