from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from projects.models import Projects
from django.views import View
from django.db.models import Q
# Create your views here.
class ProjectsView(View):

    def get(self, request):
        # 创建数据库数据
        # pro_obj = Projects(name='牛逼项目', leader='icon', tester='czd', publish_app='应用', programer='xxx',
        #          desc='这是伟大的项目')
        # pro_obj.save()
        # 增
        # Projects.objects.create(name='牛逼项目2', leader='icon', tester='czd', publish_app='应用', programer='xxx',
        #                         desc='这是伟大的项目2')

        """
        查询
        """
        # 查询所有数据   返回查询集
        a = Projects.objects.all()
        print(a[0].leader)
        # 查询一条记录  若不存在会返回异常
        b = Projects.objects.get(id=1)
        print(b)
        # 查询多条记录 filter过滤，exclude是跟filter反向查询
        c = Projects.objects.filter(tester='czd')
        print(c)
        # 模糊查询 字段后面加__  i开头表示不区分大小写
        d = Projects.objects.filter(tester__contains='g')
        print(d)
        # 跨表查询 子表查主表 查询接口为化的项目  主表查子表 在子表查
        e = Projects.objects.filter(interfaces__name__contains='化')
        print(e)
        # 关系查询 比较查询 gt大于 lt小于 gte大于等于 lte 小于等于
        f = Projects.objects.filter(id__gt=3)
        print(f)
        # 逻辑查询，多个条件查询 两个条件直接写是且的关系 用Q变量是或的关系
        g = Projects.objects.filter(tester='czd', name__contains='web')
        h = Projects.objects.filter(Q(tester='tingting') | Q(name__contains='web'))
        print(g)
        print(h)
        return HttpResponse('<h1>hello</h1>')
