from django.db import models
from django.contrib.auth.models import User, AbstractUser


class UserProfile(models.Model):
	user = models.OneToOneField(User)
	realname = models.CharField(max_length=16, null=True, blank=True)
	about_me = models.CharField(max_length=200, null=True, blank=True)
	location = models.CharField(max_length=64, null=True, blank=True)

	def __unicode__(self):
		return unicode(self.user.username)

	def follow(self, user):
		if not self.is_following(user):
			f = Follows(follower_id=self.id, followed_id=user.id)
			f.save()

	def unfollow(self, user):
		f = self.followers.filter(followed_id=user.id)
		print f
		if f:
			print 1
			f.delete()
			print 2

	def is_following(self, user):
		return bool(self.followers.filter(followed_id=user.id))

	def followed_posts(self):
		return Post.objects.select_related().filter(author=self.followers.all()).order_by('-timestamp')


class Post(models.Model):
	body = models.TextField()
	timestamp = models.DateTimeField(db_index=True, auto_now_add=True)
	author = models.ForeignKey(UserProfile, related_name='posts')

	def __unicode__(self):
		return self.author.user.username


class Follows(models.Model):
	follower = models.ForeignKey(UserProfile, related_name='followers')
	followed = models.ForeignKey(UserProfile, related_name='followed')
	timestamp = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.followed.user.username

	class Meta:
		unique_together = (("follower", "followed"),)


class Comment(models.Model):
	body = models.TextField()
	timestamp = models.DateTimeField(db_index=True, auto_now_add=True)
	author = models.ForeignKey(UserProfile, related_name='comments')
	post = models.ForeignKey(Post, related_name='comments')

	def __unicode__(self):
		return self.author.username