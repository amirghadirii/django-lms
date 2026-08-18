from blog.views import *
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('',blog_home, name="home"),
    path('<int:pid>',blog_single,name="single"),
    path("category/<str:cat_name>",blog_category, name="category"),
    path("search/",blog_search,name='search'),
    path("tag/<str:tag_name>",blog_home, name='tag'),
    path("author/<str:author_username>",blog_home,name='author'),
]
