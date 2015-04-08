from rest_framework import serializers
from django.contrib.auth.models import User
from main.models import UserProfile, Follows, Post, Comment


class UserSerializer(serializers.ModelSerializer):
	username = serializers.CharField(source='user.username')

	class Meta:
		model = UserProfile
		fields = ('url', 'username')


class PostSerializer(serializers.ModelSerializer):
	author = serializers.URLField(source='author.username')

	class Meta:
		model = Post
		fields = ('url', 'body', 'author', 'timestamp')