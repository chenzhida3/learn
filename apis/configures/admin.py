from django.contrib import admin
from configures.models import Configures
# Register your models here.

class configuresAdmin(admin.ModelAdmin):
    fields = ('name', 'author', 'request', 'interface')
    list_display = ['id', 'name', 'author', 'request', 'interface_id']


admin.site.register(Configures, configuresAdmin)