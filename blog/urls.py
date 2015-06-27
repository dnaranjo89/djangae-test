from django.conf.urls import patterns
from django.conf.urls import patterns, include, url
from blog import views

urlpatterns = patterns(None)

urlpatterns += patterns(
    '',
    url(r'^index', views.index, name='index'),
    url(r'^new-article', views.new_article, name='new_article'),

    url(r'^populate', views.populate, name='populate'),
)

