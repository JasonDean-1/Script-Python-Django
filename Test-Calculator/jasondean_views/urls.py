from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^add/$', 'calcApp.views.add', name='add'),
    url(r'^add/(\d+)/(\d+)/$', 'calcApp.views.add2', name='add2'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
