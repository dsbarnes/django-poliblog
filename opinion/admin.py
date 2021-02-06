from django.contrib import admin
from .models import Author, Article, Image, Video


class ArticleAdmin(admin.ModelAdmin):
    fields = ['title', 'body', 'author', 'date', 'slug']
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Article, ArticleAdmin)
admin.site.register(Author)
admin.site.register(Image)
admin.site.register(Video)
admin.site.register(ArticleSubHeading)