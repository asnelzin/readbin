from django.core.urlresolvers import reverse
from django.test import TestCase
from readbin.apps.bin.models import Article


class BinTestCase(TestCase):
    def setUp(self):
        Article.objects.create(title='Test Article', url='https://google.com')

    def test_view_articles_list(self):
        article = Article.objects.all()[0]

        response = self.client.get(reverse('bin:articles_list'))
        self.assertContains(response, article.title)
