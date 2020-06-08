from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published = models.DateTimeField()
    updated = models.DateTimeField(null=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to="images/%Y/%m/%d")
    display_order = models.IntegerField(default=0)
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="images"
    )

    def __str__(self):
        return self.article.title
