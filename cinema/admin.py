from django.contrib import admin
from .models import Post, Comment,Movie,Theatre,Showtime

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Movie)
admin.site.register(Theatre)
admin.site.register(Showtime)