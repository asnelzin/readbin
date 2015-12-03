from django.views.generic.list import ListView
from rest_framework.generics import CreateAPIView
from readbin.apps.bin.models import Article
from readbin.apps.bin.serializers import ArticleSerializer


class ArticlesList(ListView):
    model = Article
    template_name = 'apps/bin/articles_list.html'


class ArticleAPICreateView(CreateAPIView):
    serializer_class = ArticleSerializer
