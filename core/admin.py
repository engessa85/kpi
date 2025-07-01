from django.contrib import admin
from .models import ProjectForm, Department, UserDepartment

# Register your models here.

admin.site.register(ProjectForm)
admin.site.register(Department)
admin.site.register(UserDepartment)