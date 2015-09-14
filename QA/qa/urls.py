from django.conf.urls import patterns, url

from qa import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^next$', views.get_next),
    url(r'^check-user$', views.check_user),
    url(r'^answer$', views.create_answer),
)