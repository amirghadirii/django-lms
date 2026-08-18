from django.contrib import admin
from instructor.models import Instructor
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.



@admin.register(Instructor)
class InstructorAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    
    list_display = ('name', 'expertise', 'get_courses_count')
    search_fields = ('name', 'expertise')
    summernote_fields = ('bio',)