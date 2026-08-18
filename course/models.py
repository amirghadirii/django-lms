from django.db import models
from django.core.validators import MinValueValidator
from instructor.models import Instructor
# Create your models here.



class Course(models.Model):
    STATUS_CHOICES = (('draft', 'Draft'),('published', 'Published'),)
    CERTIFICATE_CHOICES = ((True, 'بله'),(False, 'خیر'),)
    
    title = models.CharField(max_length=255, verbose_name="عنوان دوره")
    slug = models.SlugField(unique=True, null=True, blank=True)
    instructor = models.ForeignKey('instructor.Instructor', on_delete=models.SET_NULL, null=True, blank=True, related_name='courses')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="دسته بندی")
    overview = models.TextField(verbose_name="بررسی اجمالی")
    curriculum = models.TextField(verbose_name="برنامه تحصیلی")
    image = models.ImageField(upload_to='courses/', verbose_name="تصویر دوره")
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="هزینه دوره")
    duration_hours = models.PositiveIntegerField(verbose_name="ساعت دوره")
    total_lectures = models.PositiveIntegerField(verbose_name="کل سخنرانی‌ها")
    capacity = models.PositiveIntegerField(verbose_name="تعداد صندلی‌ها")
    students_count = models.PositiveIntegerField(default=0, verbose_name="کل دانش‌آموزان")
    has_certificate = models.BooleanField(choices=CERTIFICATE_CHOICES, default=False, verbose_name="گواهینامه دارد؟")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    start_date = models.DateField(verbose_name="تاریخ شروع")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)
    
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=True, blank=True)
    def __str__(self):
        return self.name    

    
class Comment(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)], verbose_name="امتیاز")
    approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return f"نظر {self.user} برای {self.course}"