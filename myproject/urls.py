from django.conf.urls import patterns, include, url
from django.contrib import admin
from myadmin import views


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'myadmin.views.login', name='login'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social'))
)
