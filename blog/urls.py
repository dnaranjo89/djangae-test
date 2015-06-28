from django.conf.urls import patterns
from django.conf.urls import patterns, include, url
from blog import views

urlpatterns = patterns(None)

urlpatterns += patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^new-article', views.new_article, name='new_article'),
    url(r'^article/(?P<article_id>[0-9]+)/comment$', views.send_comment, name='comment'),
    url(r'^article/(?P<article_id>[0-9]+)/$', views.display_article, name='display_article'),

    url(r'^populate', views.populate, name='populate'),
)

