from django import forms
from .models import Post, Movie,PostAd, CATEGORIES, LOCATIONS
from django.forms import ModelForm


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','author','created_date',)

class BookingForm(forms.ModelForm):
    your_name = forms.CharField(label='Movie name', max_length=100)

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title','category','length',)