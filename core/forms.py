from core.models import Newsletter,contact
from django import forms
from captcha.fields import CaptchaField


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'
        
  
class CaptchaTestForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:  
        model = contact
        fields = ['name', 'email', 'subject', 'message'] 
        
