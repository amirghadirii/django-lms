from django.contrib.sitemaps import Sitemap
from course.models import Course
from django.urls import reverse

class CourseSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Course.objects.filter(status='published')

    def lastmod(self, obj):
        return obj.published_date
    
    def location(self, item):
        return reverse('course:course_details',kwargs={'slug':item.slug})