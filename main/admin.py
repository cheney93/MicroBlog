from django.contrib import admin
from models import UserProfile, Post, Follows, Comment

admin.site.register(UserProfile)
admin.site.register(Follows)
admin.site.register(Post)
admin.site.register(Comment)