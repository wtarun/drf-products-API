from django.shortcuts import render
from rest_framework.response import Response
from .models import Post, Author
from .serializers import PostSerializer, AuthorSerializer
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def list_posts(request):
    # Fetch posts
    posts = Post.objects.all()

    # serialize
    serializer = PostSerializer(posts, many=True)

    # return response
    return Response(serializer.data)
