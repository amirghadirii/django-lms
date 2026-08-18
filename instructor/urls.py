from instructor.views import *
from django.urls import path


app_name = 'instructor'



urlpatterns = [
    path('', instructor_home ,name='instructor_home' ),
    path('<str:slug>/', instructor_single ,name='instructor_single' ),
]