from django.db import models


class BlogAuthor(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=255)
    site = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



class BlogPost(models.Model):
    img = models.ImageField()
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(BlogAuthor, on_delete=models.CASCADE)

    def __str__(self):
        return self.title