from django.contrib import admin
from .models import *
admin.site.register(Information)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Competence)


class ProjectAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}
admin.site.register(Project,ProjectAdmin)
admin.site.register(Message)