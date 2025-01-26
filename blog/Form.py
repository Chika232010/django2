from .models import Blog
from django import forms

class BlogForm(forms.Form):
    titl = forms.CharField(max_length=100, label='название блога')
    descriptions = forms.CharField(widget=forms.Textarea, label='описание')
    publc = forms.BooleanField(required=True)
    

class FeedBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'descriptions', 'public', 'img']
        