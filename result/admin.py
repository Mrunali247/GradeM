from django.contrib import admin
from result.models import *
# Register your models here.
class LoginAdmin(admin.ModelAdmin):
    list_display=['ID', 'name', 'username','password', 'classTeacher']

class DepartmentAdmin(admin.ModelAdmin):
    list_display=['deptId', 'deptName']

class ClassTeacherAdmin(admin.ModelAdmin):
    list_display=['ID', 'deptId', 'semester', 'academicYear']

class SubjectsAdmin(admin.ModelAdmin):
    list_display=['subjectId', 'semester', 'subjectName', 'deptId']

admin.site.register(Subjects, SubjectsAdmin)

admin.site.register(Login, LoginAdmin)
admin.site.register(ClassTeacher, ClassTeacherAdmin)
admin.site.register(Department, DepartmentAdmin)