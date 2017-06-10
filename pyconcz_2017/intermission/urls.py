from django.conf.urls import url

from pyconcz_2017.intermission import views


urlpatterns = [
    url('^$', views.index, name='cycle_all'),
    url('^sponsors/(?P<level>\d)+/$', views.sponsors, name='sponsors'),
    url('^annoucements/$', views.announcements, name='annoucements'),
    url('^up-next/(?P<track>\d+)/$', views.up_next, name='up_next'),
    url('^workshop-sinners/$', views.workshop_sinners, name='workshop_sinners'),
]
