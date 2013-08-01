from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'^$', views.MinutesList.as_view(), name='minutes_list'),
    url(r'^(?P<year>[0-9]{4})-(?P<month>[0-9]{2})-(?P<day>[0-9]{2})/$', views.MinutesDetail.as_view(), name='minutes_detail'),
)