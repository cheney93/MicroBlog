from django.shortcuts import render
from main.models import UserProfile, Post
from rest_framework import viewsets
from serializers import UserSerializer, PostSerializer


class UserViewSet(viewsets.ModelViewSet):
	queryset = UserProfile.objects.all()
	serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
	queryset = Post.objects.all()
	serializer_class = PostSerializer