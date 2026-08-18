from django.contrib import admin
from course.models import Course, Category, Comment
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
class CourseAdmin(SummernoteModelAdmin):
    list_display = ('title','price','status','published_date','capacity', 'start_date')
    list_filter = ('category', 'has_certificate', 'start_date')
    search_fields = ('title', 'overview')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-created_at',)
    summernote_fields = ('overview','curriculum')


class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('user', 'course', 'rating', 'approved', 'created_date')
    list_filter = ('approved', 'rating', 'created_date')
    search_fields = ('text', 'user__username')
    empty_value_display = '-empty-'
    


admin.site.register(Category)    
admin.site.register(Course,CourseAdmin)
admin.site.register(Comment,CommentAdmin)