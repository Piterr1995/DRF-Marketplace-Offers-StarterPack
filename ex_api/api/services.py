"""
A sample method not yet used in serializer
"""

def create_article_image(article=None, image=None, display_order=None):
    if not display_order:
        if not article.images.all():
            display_order = 0
        else:
            display_order = max([img.display_order for img in article.images.all]) + 1
    kwargs = {"article_id": article.id, "image": image, "display_order": display_order}
    return Image.objects.create(**kwargs)
