import json

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status

from rest_framework.response import Response
from projects.models import Projects
from projects.serializer import ProjectModelSerializer
from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from rest_framework import generics
# Create your views here.
class ProjectsList(generics.ListCreateAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectModelSerializer

    ordering_fields = ['name']
    filterset_fields = ['name', 'tester', 'leader']

class ProjectsDetail(generics.RetrieveUpdateDestroyAPIView):
    """项目详情"""
    # def get_object(self, pk):
    #     try:
    #         return Projects.objects.get(id=pk)
    #     except Projects.DoesNotExist:
    #         raise Http404
    queryset = Projects.objects.all()
    serializer_class = ProjectModelSerializer
