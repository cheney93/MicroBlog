from rest_framework import serializers
from django.contrib.auth.models import User
from main.models import UserProfile, Follows, Post, Comment


class PostSerializer(serializers.HyperlinkedModelSerializer):
	author = serializers.HyperlinkedRelatedField(
		view_name='userprofile-detail',
		read_only=True,
	)
	comments = serializers.HyperlinkedRelatedField(
		view_name='comment-detail',
		read_only=True,
		many=True,
	)
	comment_count = serializers.IntegerField(
		source='comments.count',
		read_only=True,
	)

	class Meta:
		model = Post
		fields = ('url', 'body', 'timestamp', 'author', 'comments', 'comment_count')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
	post = serializers.HyperlinkedRelatedField(
		view_name='post-detail',
		read_only=True,
	)
	author = serializers.HyperlinkedRelatedField(
		view_name='userprofile-detail',
		read_only=True,
	)

	class Meta:
		model = Comment
		fields = ('url', 'post', 'body', 'timestamp', 'author')


class UserSerializer(serializers.HyperlinkedModelSerializer):
	username = serializers.CharField(
		source='user.username',
	)
	member_since = serializers.CharField(
		source='user.date_joined',
	)
	last_seen = serializers.CharField(
		source='user.last_login',
	)

	class Meta:
		model = UserProfile
		fields = ('url', 'username', 'member_since', 'last_seen')