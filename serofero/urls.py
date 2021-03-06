from django.contrib import admin
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from sf import urls as sfurls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'serofero.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(sfurls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
