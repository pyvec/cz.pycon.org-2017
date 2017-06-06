from django.conf.urls import url

from pyconcz_2017.intermission import views


urlpatterns = [
    url('^index/$', views.index, name='index'),
    url('^sponsors/(?P<level>\d)+/$', views.sponsors, name='sponsors'),
    url('^annoucements/$', views.announcements, name='annoucements'),
    url('^up-next/(?P<track>\d+)/$', views.up_next, name='up_next'),
]
