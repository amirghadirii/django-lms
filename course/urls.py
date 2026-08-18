from course.views import *
from django.urls import path

app_name = 'course'

urlpatterns = [
    path('', course_home, name="course"),
    path('<slug:slug>/', course_details, name="course_details"),
    path("category/<str:cat_name>",course_category, name="course_category"),
]