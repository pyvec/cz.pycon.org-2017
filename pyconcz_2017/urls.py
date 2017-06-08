from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView

from pyconcz_2017.common.views import homepage

prefixed_urlpatterns = [
    url(r'^$', homepage, name='homepage'),
    url(r'^announcements/', include('pyconcz_2017.announcements.urls')),
    url(r'^proposals/workshops/$', RedirectView.as_view(url='/2017/proposals/talks')),
    url(r'^proposals/', include('pyconcz_2017.proposals.urls')),

    url(r'^about/team/', include('pyconcz_2017.team.urls')),
    url(r'^speakers/', include('pyconcz_2017.speakers.urls')),
    url(r'^sponsors/', include('pyconcz_2017.sponsors.urls')),
    url(r'^intermission/', include('pyconcz_2017.intermission.urls', namespace='intermission')),

    # static pages
    url(r'^proposals/$',
        TemplateView.as_view(template_name='proposals/talks_about.html'),
        name='proposals'),
    url(r'^about/$',
        TemplateView.as_view(template_name='pages/about.html'),
        name='about'),
    url(r'^about/code/$',
        TemplateView.as_view(template_name='pages/code.html'),
        name='about_code'),
    url(r'^about/transparency_report/$',
        TemplateView.as_view(template_name='pages/transparency.html'),
        name='about_transparency'),
    url(r'^about/prague/$',
        TemplateView.as_view(template_name='pages/prague.html'),
        name='about_city'),
]

urlpatterns = (
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) +
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +
    [
        url(r'^2017/', include(prefixed_urlpatterns)),
        url(r'^admin/', include(admin.site.urls)),
        url(r'^$', RedirectView.as_view(url='/2017/')),
    ]
)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
