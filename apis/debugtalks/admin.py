from django.contrib import admin
from debugtalks.models import Debugtalks
# Register your models here.

class debugtalksAdmin(admin.ModelAdmin):
    fields = ('name', 'debugtalk', 'project')
    list_display = ['id', 'name', 'debugtalk', 'project_id']


admin.site.register(Debugtalks, debugtalksAdmin)