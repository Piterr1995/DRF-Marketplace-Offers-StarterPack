from django.contrib import admin
from .models import Article, Image

# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "published", "updated")


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("article",)
