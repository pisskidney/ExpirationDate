from django.conf.urls import patterns, include, url
from django.contrib import admin

from expirationDate.views import HomePage

urlpatterns = patterns(
    '',
    url(r'^$', HomePage.as_view(), name='home'),
    (r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
)
