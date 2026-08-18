from django.contrib.sitemaps import Sitemap
from instructor.models import Instructor
from django.urls import reverse

class InstructorSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Instructor.objects.all()

    def location(self, obj):
        # نام دقیق URL که تو urls.py هست
        return reverse('instructor:instructor_single', kwargs={'slug': obj.slug})