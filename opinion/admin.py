from django.contrib import admin
from .models import BlogAuthor, BlogPost

# Register your models here.

admin.site.register(BlogAuthor)
admin.site.register(BlogPost)