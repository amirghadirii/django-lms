from django.db import models

# Create your models here.
class Newsletter(models.Model):
    email = models.EmailField(unique=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    

class contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255,blank=True,null=True)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created_date']
    
    def __str__(self):
        return f"{self.name} - {self.subject}"