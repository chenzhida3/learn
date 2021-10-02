from django.contrib import admin
from interfaces.models import Interfaces
# Register your models here.

class InterfacesAdmin(admin.ModelAdmin):
    """定制化后台站点类"""
    fields = ('name', 'tester', 'desc', 'project')
    list_display = ['id', 'name', 'tester', 'project_id']
admin.site.register(Interfaces, InterfacesAdmin)