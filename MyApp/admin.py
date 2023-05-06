
from django.contrib import admin
from MyApp.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ["student_id","student_class","student_name","student_fathername",'student_addr','student_tuitionfee','student_busfee']

admin.site.register(Student,StudentAdmin)