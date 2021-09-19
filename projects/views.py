import json

from django.http import JsonResponse, HttpResponse, Http404
from projects.models import Projects
from projects.serializer import ProjectSerializer
from django.views import View
# Create your views here.
class ProjectsView(View):

    def get(self, request):
        project_qs = Projects.objects.all()
        # project_list = []
        # for project in project_qs:
        #     project_list.append({
        #         'name': project.name,
        #         'leader': project.leader,
        #         'tester': project.tester,
        #         'programer': project.programer,
        #         'publish_app': project.publish_app,
        #         'desc': project.desc
        #     })
        # return JsonResponse(project_list, safe=False)
        serializer = ProjectSerializer(instance=project_qs, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        """新增项目"""
        # 从前端获取json数据，转化成python的类型
        json_data = request.body.decode('utf-8')
        python_data = json.loads(json_data, encoding='utf-8')

        serializer = ProjectSerializer(data=python_data)
        # 校验前端传的参数
        # 调用序列化器的is_valid方法， 开始校验前端参数
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return JsonResponse(serializer.errors)

        # 向数据库新增项目
        # new_project = Projects.objects.create(name=python_data['name'],
        #                         leader=python_data['leader'],
        #                         tester=python_data['tester'],
        #                         programer=python_data['programer'],
        #                         publish_app=python_data['publish_app'],
        #                         desc=python_data['desc'])
        project = Projects.objects.create(**serializer.validated_data)

        serializer = ProjectSerializer(instance=project)
        return JsonResponse(serializer.data, status=201)

class ProjectsDetail(View):
    """项目详情"""
    def get_object(self, pk):
        try:
            return Projects.objects.get(id=pk)
        except Projects.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """获取项目详情"""
        # 1、校验pk  省略
        project = self.get_object(pk)
        # one_dict = {
        #     'name': project.name,
        #     'leader': project.leader,
        #     'tester': project.tester,
        #     'programer': project.programer,
        #     'publish_app': project.publish_app,
        #     'desc': project.desc
        # }
        # 1.通过模型类对象或者查询集传给instance，就可以进行序列化输出
        # 2.通过序列化器对象的data属性，就可以获得字典
        serializer = ProjectSerializer(instance=project)
        return JsonResponse(serializer.data)

    # 更新
    def put(self, request, pk):
        project = self.get_object(pk)
        # 从前端获取json数据，转化成python的类型
        json_data = request.body.decode('utf-8')
        python_data = json.loads(json_data, encoding='utf-8')

        serializer = ProjectSerializer(data=python_data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return JsonResponse(serializer.errors)

        project.name = serializer.validated_data['name']
        project.leader = serializer.validated_data['leader']
        project.tester = serializer.validated_data['tester']
        project.programer = serializer.validated_data['programer']
        project.publish_app = serializer.validated_data['publish_app']
        project.desc = serializer.validated_data['desc']
        project.save()
        # one_dict = {
        #     'name': project.name,
        #     'leader': project.leader,
        #     'tester': project.tester,
        #     'programer': project.programer,
        #     'publish_app': project.publish_app,
        #     'desc': project.desc
        # }
        serializer = ProjectSerializer(instance=project)
        return JsonResponse(serializer.data, status=201)

    def delete(self, request, pk):
        project = self.get_object(pk)
        project.delete()
        return JsonResponse(None, safe=False, status=204)