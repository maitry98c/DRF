from django.shortcuts import render
from rest_framework import generics, status
import requests
from django.http import JsonResponse, HttpResponse, Http404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import postId,Comments
from .serializers import PostSerializer, CommentSerializer


def Index(request):
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    serializer = PostSerializer(data=r.json(),many=True)
    serializer.is_valid(True)
    if (serializer.save()):
        return HttpResponse("Successfully added posts, In order to view posts, go to the api http://127.0.0.1:8000/posts ")
    else:
        return HttpResponse("oops")


def IndexComment(request):
    r = requests.get("https://jsonplaceholder.typicode.com/comments")
    # return HttpResponse(r.json())
    serializer = CommentSerializer(data=r.json(), many=True)
    serializer.is_valid(True)
    if (serializer.save()):
        return HttpResponse("Successfully added Comments, In order to view posts, go to the api http://127.0.0.1:8000/comments  ")
    else:
        return HttpResponse("oops")

class PostList(generics.ListAPIView):
    queryset = postId.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = postId.objects.all()



class CommentsList(generics.ListAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer


class CommentsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer


class CommentsEach(generics.RetrieveUpdateDestroyAPIView):
    lookup_fields = 'postId'
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer



