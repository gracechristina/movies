from django import forms
from .models import Post, PostAd, CATEGORIES, LOCATIONS
from django.forms import ModelForm


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','author',)

class BookingForm(forms.Form):
    your_name = forms.CharField(label='Movie name', max_length=100)