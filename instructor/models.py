from django.db import models
from django.utils.text import slugify
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Instructor(models.Model):
    name = models.CharField(max_length=100,verbose_name="نام مدرس")
    slug = models.SlugField(max_length=255, allow_unicode=True, null=True, blank=True)
    bio = models.TextField(verbose_name="بیوگرافی")
    image = models.ImageField(upload_to='instructors/',verbose_name="عکس")
    expertise = models.CharField(max_length=200,verbose_name="تخصص")
    number = PhoneNumberField(region='IR',blank=True, null=True, verbose_name="شماره تماس")
    email = models.EmailField(blank=True, null=True,verbose_name="ایمیل ")
    website = models.URLField(blank=True, null=True,verbose_name="آدرس سایت")
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    def get_courses_count(self):
        return self.courses.filter(status='published').count()

    def get_total_students(self):
        from django.db.models import Sum
        total = self.courses.aggregate(total=Sum('students_count'))['total']
        return total if total else 0