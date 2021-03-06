"""learn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path, include
#
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('user/', include('user.urls'))
# ]
from django.urls import path, include, re_path
from django.contrib import admin
from rest_framework import routers, permissions
from rest_framework.documentation import include_docs_urls
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from user import views

router = routers.DefaultRouter()
router.register('api_info', views.RegisterView)

schema_view = get_schema_view(
    openapi.Info(
        title="测试平台API",
        default_version='v1.0',
        description="测试工程接口文档",
        terms_of_service="#",
        contact=openapi.Contact(email="chenzhida3@163.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # 配置django-rest-framwork API路由
    path('user/', include('user.urls')),
    path('projects/', include('projects.urls')),
    path('interface/', include('interfaces.urls')),
    path('envs/', include('envs.urls')),
    path('debugtalk/', include('debugtalks.urls')),
    path('testsuit/', include('testsuits.urls')),
    path('reports/', include('reports.urls')),
    path('configures/', include('configures.urls')),
    path('testcases/', include('testcases.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('docs/', include_docs_urls(title='测试平台接口文档')),
    # 配置drf-yasg路由
    # re_path('^swagger(?P<format>\.json|\.yaml)$', schema_view.with_ui(cache_timeout=0), name='schema-json'),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]