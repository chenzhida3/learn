import json

from django.http import JsonResponse, HttpResponse, Http404
from projects.models import Projects
from projects.serializer import ProjectSerializer
from django.views import View
# Create your views here.
class ProjectsView(View):

    # 获取所有项目
    def get(self, request):
        project_qs = Projects.objects.all()
        serializer = ProjectSerializer(instance=project_qs, many=True)
        return JsonResponse(serializer.data, safe=False)

    # 创建
    def post(self, request):
        """新增项目"""
        json_data = request.body.decode('utf-8')
        python_data = json.loads(json_data, encoding='utf-8')

        serializer = ProjectSerializer(data=python_data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return JsonResponse(serializer.errors)
        serializer.save()
        return JsonResponse(serializer.data, status=201)

class ProjectsDetail(View):
    """项目详情"""
    def get_object(self, pk):
        try:
            return Projects.objects.get(id=pk)
        except Projects.DoesNotExist:
            raise Http404

    # 获取单个详情
    def get(self, request, pk):
        """获取项目详情"""
        # 1、校验pk  省略
        project = self.get_object(pk)
        serializer = ProjectSerializer(instance=project)
        return JsonResponse(serializer.data)

    # 更新
    def put(self, request, pk):
        project = self.get_object(pk)
        # 从前端获取json数据，转化成python的类型
        json_data = request.body.decode('utf-8')
        python_data = json.loads(json_data, encoding='utf-8')

        serializer = ProjectSerializer(instance=project, data=python_data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return JsonResponse(serializer.errors)
        serializer.save()
        return JsonResponse(serializer.data, status=201)

    # 删除
    def delete(self, request, pk):
        project = self.get_object(pk)
        project.delete()
        return JsonResponse(None, safe=False, status=204)