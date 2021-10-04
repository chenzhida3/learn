from django.contrib import admin
from reports.models import Reports
# Register your models here.

class reportsAdmin(admin.ModelAdmin):
    fields = ('name', 'result', 'count', 'success', 'html', 'summary')
    list_display = ['id', 'name', 'result', 'count']


admin.site.register(Reports, reportsAdmin)