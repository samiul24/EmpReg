from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from EmpInfo.models import District, Thana, Department, Designation, EmpBasicInfo, EmpSalary, \
     EmpEducation, Student, Card, Blog, Author, Entry

# Register your models here.
class DistrictAdmin(admin.ModelAdmin):
    list_display=['id', 'name']
    list_filter=['id', 'name']
    search_fields = ['name']
    ordering = ['id'] 

class ThanaAdmin(admin.ModelAdmin):
    list_display=['id','district','name']
    list_filter=['id','district','name']
    ordering = ['id'] 

class DepartmentAdmin(admin.ModelAdmin):
    list_display=['id','name']
    list_filter=['id','name']
    ordering = ['id'] 

class DesignationAdmin(admin.ModelAdmin):
    list_display=['id','name']
    list_filter=['id','name']
    ordering = ['id']

class EmpBasicInfoAdmin(admin.ModelAdmin):
    list_display=[
                    'id', 'emp_id','first_name', 'last_name', 
                    'dob_tag', 'image_tag', 'phone', 'email', 
                    'thana', 'district', 'joiningdate_tag', 
                    'department', 'designation', 'status'
            ]

class EmpSalaryAdmin(admin.ModelAdmin):
    list_display=['employee', 'basicsalary', 'medical', 'houserent', 'others', ]

class EmpEducationAdmin(admin.ModelAdmin):
    list_display=['employee', 'degree', 'institute', 'passingyear', 'result']

class StudentAdmin(admin.ModelAdmin):
    list_display=['year_in_school', 'is_upperclass']

class CardAdmin(admin.ModelAdmin):
    list_display=['suit']

"""class BlogAdmin(admin,ModelAdmin):
    list_display=['name']

class AuthorAdmin(admin,ModelAdmin):
    list_display=['name']

class EntryAdmin(admin,ModelAdmin):
    list_display=['headline']"""

admin.site.register(District, DistrictAdmin)
admin.site.register(Thana, ThanaAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Designation, DesignationAdmin)
admin.site.register(EmpBasicInfo, EmpBasicInfoAdmin)
admin.site.register(EmpSalary, EmpSalaryAdmin)
admin.site.register(EmpEducation, EmpEducationAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Card, CardAdmin)
"""admin.site.register(Blog, BlogAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Entry, EntryAdmin)"""
