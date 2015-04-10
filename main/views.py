# coding: utf-8
from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib import messages

from main.models import UserProfile, Post, Follows, Comment


def index(request):
	if request.method == "POST":
		userid = get_object_or_404(User, username=request.user)
		body = request.POST.get('body')
		p = Post()
		p.author = userid
		p.body = body
		p.save()
		return HttpResponseRedirect('/')
	show_followed = False
	if str(request.user) != 'AnonymousUser':
		u = UserProfile.objects.get(user__username=request.user)
		show_cookie = bool(request.COOKIES.get('show_followed', ''))
		if show_cookie:
			posts = u.followed_posts()
		else:
			posts = Post.objects.order_by('-timestamp')
	return render_to_response(
		'index.html',
		locals(),
		context_instance=RequestContext(request))


@login_required(login_url='/account/login')
def user_view(request, username):
	username = username.encode('utf-8')
	user = get_object_or_404(User, username=username)
	postsList = []
	posts = Post.objects.filter(author=user.id).order_by('-timestamp')
	for i in posts:
		postsList.append(i)
	user = UserProfile.objects.get_or_create(user__username=user.username, user_id=user.id)[0]
	u = UserProfile.objects.get(user__username=request.user)
	f = u.is_following(user)
	return render_to_response(
		'user.html',
		{'user': user, 'posts': postsList, 'f': f},
		context_instance=(RequestContext(request)))


@login_required(login_url='/account/login')
def edit_profile(request):
	if request.method == 'POST':
		username = request.user
		realname = request.POST.get('realname')
		location = request.POST.get('location')
		about_me = request.POST.get('about_me')
		userObj = get_object_or_404(UserProfile, user=username)
		userObj.realname = realname
		userObj.location = location
		userObj.about_me = about_me
		userObj.save()
		messages.success(request, '编辑成功!')
		return HttpResponseRedirect('/user/%s' % username)
	return render_to_response('edit_profile.html', context_instance=(RequestContext(request)))


@login_required(login_url='/account/login')
def post(request, postid):
	post = get_object_or_404(Post, id=postid)
	if request.method == "POST":
		u = UserProfile.objects.get(user__username=request.user)
		comment_body = request.POST.get('body')
		print comment_body
		comment = Comment(body=comment_body, author=u.user, post=post)
		comment.save()
		messages.success(request, '成功发表评论!')
		return HttpResponseRedirect('/post/%s' % postid)
	comments = []
	commentObj = post.comments.order_by('timestamp')
	for i in commentObj:
		comments.append(i)
	return render_to_response(
		'post.html',
		{'post': post, 'comments': comments},
		context_instance=(RequestContext(request)))


@login_required(login_url='/account/login')
def follow(request, username):
	current_user = UserProfile.objects.get(user__username=request.user)
	u = UserProfile.objects.get(user__username=username)
	if u is None:
		messages.error(request, '无效的用户!')
		return HttpResponseRedirect('/')
	if current_user.is_following(u):
		messages.warning(request, '已经关注过他了!')
		return HttpResponseRedirect('/')
	current_user.follow(u)
	messages.success(request, '成功关注%s!' % u.user)
	return HttpResponseRedirect('/user/%s' % u.user)


@login_required(login_url='/account/login')
def unfollow(request, username):
	current_user = UserProfile.objects.get(user__username=request.user)
	u = UserProfile.objects.get(user__username=username)
	if u is None:
		messages.error(request, '无效的用户!')
		return HttpResponseRedirect('/')
	if not current_user.is_following(u):
		messages.warning(request, '本来就没有关注他!')
		return HttpResponseRedirect('/')
	current_user.unfollow(u)
	messages.success(request, '你不再关注%s!' % u.user)
	return HttpResponseRedirect('/user/%s' % u.user)


@login_required(login_url='/account/login')
def followers(request, username):
	u = UserProfile.objects.get(user__username=username)
	if u is None:
		messages.error(request, '无效的用户!')
		return HttpResponseRedirect('/')
	follows = u.followed.all()
	followList = []
	for item in follows:
		followList.append({'user': item.follower, 'timestamp': item.timestamp})
	return render_to_response(
		'followers.html',
		{'followList': followList, 'user': u, 'title': '的粉丝列表'},
		context_instance=(RequestContext(request)))


@login_required(login_url='/account/login')
def followed_by(request, username):
	u = UserProfile.objects.get(user__username=username)
	if u is None:
		messages.error(request, '无效的用户!')
		return HttpResponseRedirect('/')
	follows = u.followers.all()
	followList = []
	for item in follows:
		followList.append({'user': item.followed, 'timestamp': item.timestamp})
	return render_to_response(
		'followers.html',
		{'followList': followList, 'user': u, 'title': '的关注列表'},
		context_instance=(RequestContext(request)))


@login_required(login_url='/account/login')
def show_all(request):
	resp = HttpResponseRedirect('/')
	resp.set_cookie('show_followed', '', max_age=30 * 24 * 60 * 60)
	return resp


@login_required(login_url='/account/login')
def show_followed(request):
	resp = HttpResponseRedirect('/')
	resp.set_cookie('show_followed', '1', max_age=30 * 24 * 60 * 60)
	return resp