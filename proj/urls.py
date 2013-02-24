from django.conf.urls import patterns, include, url
from bookapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bookfairy.views.home', name='home'),
    # url(r'^bookfairy/', include('bookfairy.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'bookapp.views.enter_search'),
    url(r'^booklist/$', 'bookapp.views.check_books'),
    # url(r'^booklist/$', views.make_booklist, name='booklist'),
    # url(r'^booksearch/$', views.upload_file),
    # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #?
)

# Example on StackOverflow has a urls.py in the project folder 
# as well as the ap folder for the Project URLs and the App URLs
# the below is for the App URLs
# # -*- coding: utf-8 -*-
# from django.conf.urls.defaults import patterns, url

# urlpatterns = patterns('myapp.views',
#     url(r'^list/$', 'list', name='list'),
# )

urlpatterns += staticfiles_urlpatterns()

if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
