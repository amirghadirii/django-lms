from core.views import *
from django.urls import path


app_name = 'core'



urlpatterns = [
    path('', index_view ,name='index' ),
    path('contact/', contact_view ,name='contact'),
    path('about/', about_view ,name='about'),
    path('faq/', faq_view ,name='faq'),
    path('newsletter/', newsletter_view, name='newsletter'),
    path("search/",search_view,name='search'),
]