from django.contrib import admin

from .models import Department, Projects


# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Department, DepartmentAdmin)


class ProjectAdmin(admin.ModelAdmin):
    pass


admin.site.register(Projects, ProjectAdmin)
