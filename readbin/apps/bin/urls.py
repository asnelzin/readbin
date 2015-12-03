from django.conf.urls import patterns, url
from readbin.apps.bin.views import ArticlesList, ArticleAPICreateView

urlpatterns = patterns('',
                       url(r'^$', ArticlesList.as_view(), name='articles_list'),
                       url(r'^add/$', ArticleAPICreateView.as_view(), name='article_create'))
