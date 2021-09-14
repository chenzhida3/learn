from django.contrib import admin
from projects.models import Projects

# Register your models here.
class ProjectsAdmin(admin.ModelAdmin):
    fields = ('name', 'leader', 'programer', 'publish_app', 'tester', 'desc')
    list_display = ['name', 'leader', 'tester', 'publish_app']
admin.site.register(Projects, ProjectsAdmin)
