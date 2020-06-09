from rest_framework import serializers
from .models import Article, Image
from django.contrib.auth.models import User
from drf_extra_fields.fields import Base64ImageField
from django.utils import timezone
import pdb



class MultiImageSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    # image = Base64ImageField(required=False)
    display_order = serializers.IntegerField(required=False)
    image = serializers.ImageField(required=False)


class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=2000)
    published = serializers.DateTimeField(required=False)
    updated = serializers.DateTimeField(required=False)
    author_username = serializers.SerializerMethodField()
    images = MultiImageSerializer(many=True, required=False)
    delete_images_pk = serializers.ListField(required=False)
    delete_images_display_order = serializers.ListField(required=False)

    def get_author_username(self, instance):
        return instance.author.username

    def create(self, validated_data):
        request = self.context.get("request")
        images = request.data.getlist("images")
        article = Article.objects.create(published=timezone.now(), **validated_data)
        if images:
            for index, image in enumerate(images):
                Image.objects.create(article=article, image=image, display_order=index)
        return article

    def update(self, instance, validated_data):
        request = self.context.get("request")
        images = request.data.getlist("images")
        vd = validated_data
        instance.title = vd.get("title", instance.title)
        instance.description = vd.get("description", instance.title)
        instance.updated = timezone.now()
        delete_images_pk = vd.get("delete_images_pk")
        delete_images_display_order = vd.get("delete_images_display_order")
        if delete_images_pk:
            for image_pk in delete_images_pk:
                Image.objects.get(pk=image_pk).delete()
        if delete_images_display_order:
            for image_display_order in delete_images_display_order:
                Image.objects.get(article=instance, display_order=image_display_order).delete()
        if images:
            for image in images:
                display_order = len(instance.images.all()) + 1
                Image.objects.create(article=instance, image=image, display_order=display_order)
        pdb.set_trace()
        return instance
