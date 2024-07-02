from django.contrib import admin
from .models import Department, BranchDepartment, Course

# Register your models here.
admin.site.register(Department)
admin.site.register(BranchDepartment)
admin.site.register(Course)
