from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.ArticleAPIView.as_view()),
    path("<int:pk>/", views.ArticleDetailView.as_view()),
    path("image-detail/<int:pk>/", views.ImageDetailView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
