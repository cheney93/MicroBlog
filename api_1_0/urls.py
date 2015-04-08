from django.conf.urls import patterns, url, include
from rest_framework import routers
from api_1_0 import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'posts', views.PostViewSet)

urlpatterns = patterns(
	'',
	url(r'^', include(router.urls)),
)
