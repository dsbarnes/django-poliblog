from django.db import models
from django.utils.text import slugify


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
    date = models.DateField()
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Do I want to have the datetime set?
        # Or should I be able to pick, so that I can backdate?
        # leaving commented out for now.
        if not self.id:
            self.slug = slugify(self.title)
            # self.date = datetime.now()
        super(Article, self).save(*args, **kwargs)