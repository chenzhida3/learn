from django.contrib import admin
from testcases.models import TestCases
# Register your models here.


class TestCasesAdmin(admin.ModelAdmin):
    fields = ('name', 'include', 'author', 'interface')
    list_display = ['id', 'name', 'include', 'author', 'interface_id']


admin.site.register(TestCases, TestCasesAdmin)