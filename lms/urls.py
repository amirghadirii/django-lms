"""
URL configuration for lms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from core import views
from core.sitemaps import StaticViewSitemap
from django.contrib.sitemaps.views import sitemap
from debug_toolbar.toolbar import debug_toolbar_urls
from blog.sitemaps import BlogSitemap
from course.sitemaps import CourseSitemap
from instructor.sitemaps import InstructorSitemap

sitemaps = {
    "static": StaticViewSitemap,
    "blog": BlogSitemap,
    "instructor": InstructorSitemap,
    }

handler404 = "core.views.page_not_found"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('core.urls')),
    path('blog/',include('blog.urls')),
    path('accounts/',include('allauth.urls')),
    path('course/',include('course.urls')),
    path('instructor/',include('instructor.urls')),
    
    path("sitemap.xml",sitemap,{"sitemaps": sitemaps},name="django.contrib.sitemaps.views.sitemap",),
    path('robots.txt',include('robots.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('captcha/', include('captcha.urls')),
    path('maintenance/', views.maintenance, name='maintenance'),
    
]+ debug_toolbar_urls()


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)