from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from .models import Article, Image
from rest_framework.response import Response
from .serializers import ArticleSerializer, MultiImageSerializer
from rest_framework import status
from rest_framework.parsers import (
    FormParser,
    MultiPartParser,
)


class ArticleAPIView(generics.ListCreateAPIView):
    parser_classes = [FormParser, MultiPartParser]
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ImageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = MultiImageSerializer
    lookup_field = "pk"



"""
ALTERNATIVE WAY WITH MORE FLEXIBILITY USING APIView
"""

# class ArticleAPIView(APIView):
#     parser_classes = [
#         FormParser,
#         MultiPartParser,
#         FileUploadParser,
#     ]

#     def get(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ArticleSerializer(
#             data=request.data,
#             context={
#                 "request": self.request
#             },  # przekazuję dane requesta do serializera
#         )
#         if serializer.is_valid():
#             serializer.save(author=self.request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# class ArticleDetailView(APIView):
#     def get_object(self, pk):
#         try:
#             return Article.objects.get(pk=pk)
#         except Article.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def put(self, request, pk):
#         article = self.get_object(pk=pk)
#         serializer = ArticleSerializer(instance=article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def get(self, request, pk):
#         article = self.get_object(pk=pk)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     def delete(self, request, pk):
#         article = self.get_object(pk=pk)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
