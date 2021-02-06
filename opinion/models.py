from django.db import models
from django.utils.text import slugify
from django.contrib.postgres.fields import ArrayField

class Author(models.Model):
    first_name  =   models.CharField(max_length=25)
    last_name   =   models.CharField(max_length=25)
    email       =   models.CharField(max_length=255, blank=True)
    site        =   models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Article(models.Model):
    title   =   models.CharField(max_length=255)
    body    =   models.TextField()
    author  =   models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    date    =   models.DateField()
    slug    =   models.SlugField(blank=False, null=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
            # If you want the date to save when article is saved, uncomment below
            # self.date = datetime.now()
        super(Article, self).save(*args, **kwargs)


class Video(models.Model):
    article     =   models.ForeignKey(Article, on_delete=models.CASCADE)
    vid         =   models.UUIDField()
    name        =   models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Image(models.Model):
    article     =   models.ForeignKey(Article, on_delete=models.CASCADE)
    img         =   models.ImageField(upload_to='img/')
    name        =   models.CharField(max_length=25)

    def __str__(self):
        return self.name


# This is one, probably poor idea
# class ArticleSubHeading(models.Model):
#     article   =   models.ForeignKey(Article, on_delete=models.CASCADE)
#     text      =   models.CharField(max_length=25)
#     name      =   models.CharField(max_length=25)

#     def __str__(self):
#         return self.name