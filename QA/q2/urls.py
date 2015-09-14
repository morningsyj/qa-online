from django.conf.urls import patterns, url

from q2 import views2

urlpatterns = patterns('',
    url(r'^$', views2.index, name='index'),
    url(r'^next$', views2.get_next),
    url(r'^check-user$', views2.check_user),
    url(r'^answer$', views2.create_answer),
    url(r'^fetch-data$', views2.get_data),
)
