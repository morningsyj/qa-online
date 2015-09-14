from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ImgAlgoQA.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^qa/', include('qa.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^q2/', include('q2.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
