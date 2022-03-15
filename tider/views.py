from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Comment, Subreddit
from django.contrib.auth.models import User
from .serializers import PostSerializer, CommentSerializer, SubredditSerializer, RegisterSerializer # UserSerializer, 
from rest_framework.permissions import AllowAny

# class UserCreate( generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UserList(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny)
    serializer_class = RegisterSerializer

class PostCreate( generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentCreate(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class SubredditCreate( generics.ListCreateAPIView):
    queryset = Subreddit.objects.all()
    serializer_class = SubredditSerializer

class SubredditList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subreddit.objects.all()
    serializer_class = SubredditSerializer