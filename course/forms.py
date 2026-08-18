from django import forms
from course.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['rating','text']  