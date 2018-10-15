from django.conf.urls import include, url
from django.contrib import admin
from mohome.views import home_view

urlpatterns = [
    # Examples:
    # url(r'^$', 'motobaku.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home_view),
]
