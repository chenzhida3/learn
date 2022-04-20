from django.contrib import admin
from testsuits.models import Testsuits
# Register your models here.


class TestsuitsAdmin(admin.ModelAdmin):
    fields = ('name', 'include', 'project')
    list_display = ['id', 'name', 'include', 'project_id']


admin.site.register(Testsuits, TestsuitsAdmin)