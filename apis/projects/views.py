from rest_framework.viewsets import ModelViewSet
from projects.models import Projects
from projects.serializer import ProjectModelSerializer
# Create your views here.


class ProjectsViewSet(ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectModelSerializer

    ordering_fields = ['name']
    filterset_fields = ['name', 'tester', 'leader']
