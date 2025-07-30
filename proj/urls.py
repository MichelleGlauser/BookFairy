from django.conf.urls import include, url
from bookapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.static import serve

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'bookfairy.views.home', name='home'),
    # url(r'^bookfairy/', include('bookfairy.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.enter_search, name='home'),
    url(r'^booklist/$', views.check_books, name='check_books'),
    url(r'^register/$', views.registration, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', LogoutView.as_view(template_name='logout.html'), name='logout'),
    url(r'^profile/$', views.show_profile, name='profile'),
    # Django-registration URLs
    url(r'^accounts/', include('django_registration.backends.activation.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    # url(r'^accounts/profile/$', redirect_to, {'url':'{'template_name': 'profile.html'})
    # url(r'^booklist/$', views.make_booklist, name='booklist'),
    # url(r'^booksearch/$', views.upload_file),
    # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #?
]

# Example on StackOverflow has a urls.py in the project folder 
# as well as the app folder for the Project URLs and the App URLs
# the below is for the App URLs
# # -*- coding: utf-8 -*-
# from django.conf.urls.defaults import patterns, url

# urlpatterns = patterns('myapp.views',
#     url(r'^list/$', 'list', name='list'),
# )

urlpatterns += staticfiles_urlpatterns()

if not settings.DEBUG:
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    ]
