from django.views.generic.list import ListView
from readbin.apps.bin.models import Article


class ArticlesList(ListView):
    model = Article
    template_name = 'apps/bin/articles_list.html'
