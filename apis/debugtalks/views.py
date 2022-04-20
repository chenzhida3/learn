from django.shortcuts import render

# Create your views here.
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from debugtalks.models import Debugtalks
from debugtalks.serializer import DebugtalksSerializers
from rest_framework import permissions


class DebugTalksviewset(mixins.ListModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.RetrieveModelMixin,
                        GenericViewSet):

    queryset = Debugtalks.objects.filter(is_delete=False).order_by('id')
    serializer_class = DebugtalksSerializers
    permission_classes = (permissions.AllowAny,)
    order_fields = ('id', 'project_id')

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        data_dict = {
            'id': instance.id,
            'debugtalk': instance.debugtalk
        }
        return Response(data_dict)
