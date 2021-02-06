from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=255)
    site = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



class Article(models.Model):
    img = models.ImageField()
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    slug = models.SlugField()

    def __str__(self):
        return self.title