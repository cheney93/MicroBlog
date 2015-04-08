# coding=utf-8
from django.shortcuts import HttpResponse, render_to_response, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages
# Create your views here.


def login(request):
	data = {'loginStatus': ''}
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return HttpResponseRedirect('/')
		data['loginStatus'] = u'用户名或密码错误!'
	return render_to_response('account/login.html', data, context_instance=RequestContext(request))


@login_required(login_url='/account/login')
def logout(request):
	user = request.user
	messages.success(request, '再见,%s!' % user)
	auth.logout(request)
	return HttpResponseRedirect('/')


def register(request):
	data = {'registerStatus': ''}
	if request.method == "POST":
		username = request.POST.get('username')
		p1 = request.POST.get('password1')
		p2 = request.POST.get('password2')
		user = User.objects.filter(username=username)
		if not user and p1 == p2:
			p = make_password(p1)
			u = User(username=username, password=p)
			u.save()
			messages.success(request, '注册成功!')
			return HttpResponseRedirect('/')
		else:
			data['registerStatus'] = "用户已存在或两次密码输入不一样!"
	return render_to_response('account/register.html', data, context_instance=(RequestContext(request)))