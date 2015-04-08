from django.conf.urls import patterns, url

from main import views


urlpatterns = patterns(
	'',
	url(r'^$', views.index),
	url(r'^user/(?P<username>\w+)/$', views.user_view),
	url(r'^edit_profile/$', views.edit_profile),
	url(r'^post/(?P<postid>\d+)/$', views.post),
	url(r'^follow/(?P<username>\w+)/$', views.follow),
	url(r'^unfollow/(?P<username>\w+)/$', views.unfollow),
	url(r'^followers/(?P<username>\w+)/$', views.followers),
	url(r'^followed-by/(?P<username>\w+)/$', views.followed_by),
	url(r'^show-all/$', views.show_all),
	url(r'^show-followed/$', views.show_followed),
)
