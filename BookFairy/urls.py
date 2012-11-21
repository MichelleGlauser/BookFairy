from django.conf.urls import patterns, include, url
from bookapp import views

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
    url(r'^$', views.enter_search),
    url(r'^booklist$', views.check_books, name='booklist'),
    url(r'^listsearch$', views.upload_file),
    url(r'^booksearch$', views.handle_uploaded_file),
)