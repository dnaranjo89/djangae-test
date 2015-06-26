from django.conf.urls import patterns
from django.conf.urls import patterns, include, url
from blog import views

urlpatterns = patterns(None)

urlpatterns += patterns(
    '',
    url(r'^index', views.index, name='index'),
)

