from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from news_api import models, serializers

# Create your views here.

# Function Based view

@api_view(["GET", "POST"])
def article_list_api_view(request):
    if request.method == "GET":
        articles = models.Article.objects.all()
        serializer = serializers.Article_serializers(articles, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = serializers.Article_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(["GET", "PUT", "DELETE"])
def article_details_api_view(request, pk):
    try:
        article = models.Article.objects.get(pk=pk)
    except models.Article.DoesNotExist:
        return Response({
            "error" : {
                "code" : 404,
                "message" : "Article Not Found!",
            }
        }, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = serializers.Article_serializers(article)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = serializers.Article_serializers(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    



# Class Based APIViews

class ArticleListCreateAPIView(APIView):
    def get(self, request):
        articles = models.Article.objects.all()
        serializer = serializers.ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = serializers.ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ArticleDetailsAPIView(APIView):

    def get_object(self, request, pk):
        article = get_object_or_404(models.Article, pk=pk)
        return article
    
    def get(self, request, pk):
        article = self.get_object(request, pk)
        serializer = serializers.ArticleSerializer(article)
        return Response(serializer.data)
    
    def put(self, request, pk):
        article = self.get_object(request, pk)
        serializer = serializers.ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        article = self.get_object(request, pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    




class JournalistListCreateAPIView(APIView):
    def get(self, request):
        journalists = models.Journalist.objects.all()
        serializer = serializers.JournalistSerializer(journalists, many=True, context={"request":request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = serializers.JournalistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    