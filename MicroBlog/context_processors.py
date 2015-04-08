from django.shortcuts import get_object_or_404
from main.models import UserProfile, User


def auston_proc(request):
	if str(request.user) != 'AnonymousUser':
		user = get_object_or_404(User, username=request.user)
		user = UserProfile.objects.get_or_create(user__username=user.username, user_id=user.id)[0]
		return {
			'current_user': user,
		}
	return {
		'cuttent_user': request.user
	}
