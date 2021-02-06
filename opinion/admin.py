from django.contrib import admin
from .models import Author, Article


class ArticleAdmin(admin.ModelAdmin):
    fields = ['img', 'title', 'body', 'author', 'date', 'slug']
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Author)
admin.site.register(Article, ArticleAdmin)