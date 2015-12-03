from django.conf.urls import patterns, url
from readbin.apps.bin.views import ArticlesList


urlpatterns = patterns('',
                       url(r'^$', ArticlesList.as_view(), name='articles_list'))
