from rest_framework import serializers
from readbin.apps.bin.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'url')
