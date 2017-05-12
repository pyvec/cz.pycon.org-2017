from django.conf.urls import url
from django.views.generic import RedirectView

from pyconcz_2017.speakers.views import speakers_list, schedule, talk_detail

urlpatterns = [
    url('^$', RedirectView.as_view(pattern_name='speakers_list'), {'type': 'talks'}),
    url('^(?P<type>(talks|workshops))/$', speakers_list, name="speakers_list"),
    url('^detail/(?P<type>(talk|workshop))/(?P<talk_id>\d+)/$', talk_detail, name='talk_detail'),
    url('^schedule/$', schedule, name="speakers_schedule"),
]
