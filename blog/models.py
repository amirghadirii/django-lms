from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()

class Profile(models.Model):
    ROLE_CHOICES = (
        ('student', 'دانشجو'),
        ('teacher', 'استاد'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='profiles/', blank=True, null=True, default='profiles/default.jpg')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')

    def __str__(self):
        return f"Profile of {self.user.username}"
    
    
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to= 'blog/',default = 'blog/default.jpg')
    title = models.CharField (max_length=255)
    content = models.TextField()
    tags = TaggableManager()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    counted_views = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']
        
        
        
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.name