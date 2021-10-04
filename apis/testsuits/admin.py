from django.contrib import admin
from testsuits.models import Testsuits
# Register your models here.


class TestsuitsAdmin(admin.ModelAdmin):
    fields = ('name', 'include', 'request', 'project')
    list_display = ['id', 'name', 'include', 'request', 'project_id']


admin.site.register(Testsuits, TestsuitsAdmin)