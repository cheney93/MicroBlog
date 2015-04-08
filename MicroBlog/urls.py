from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
	'',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^account/', include('account.urls')),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^api/', include('api_1_0.urls')),
	url(r'', include('main.urls')),
)
