# coding=utf-8

from django.core.urlresolvers import reverse
from django.test import TestCase
from readbin.apps.bin.models import Article

from rest_framework.test import APIClient


class BinTestCase(TestCase):
    def setUp(self):
        self.api_client = APIClient()

    def test_view_articles_list(self):
        article = Article.objects.create(title='Test Article', url='https://google.com')

        response = self.client.get(reverse('bin:articles_list'))
        self.assertContains(response, article.title)

    def test_create_article_positive(self):
        data = {'title': 'Test', 'url': 'https://google.com/'}
        response = self.api_client.post(reverse('bin:article_create'), data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, dict({'id': 1}, **data))

    def test_create_article_empty_request_negative(self):
        data = {}
        response = self.api_client.post(reverse('bin:article_create'), data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, {'title': ['This field is required.'],
                                         'url': ['This field is required.']})
