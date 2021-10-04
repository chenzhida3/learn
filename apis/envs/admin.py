from django.contrib import admin
from envs.models import Envs
# Register your models here.

class envsAdmin(admin.ModelAdmin):
    fields = ('name', 'base_url', 'desc')
    list_display = ['id', 'name', 'base_url', 'desc']


admin.site.register(Envs, envsAdmin)