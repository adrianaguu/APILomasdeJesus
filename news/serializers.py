from rest_framework import serializers
from .models import Category, News

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        


class NewsSerializer(serializers.ModelSerializer):
    urlImage_wide = serializers.SerializerMethodField('get_imagew_url')
    urlImage_medium = serializers.SerializerMethodField('get_imagem_url')
    urlImage_narrow = serializers.SerializerMethodField('get_imagen_url')

    class Meta:
        model = News
        fields = '__all__'

    def get_imagew_url(self, obj):
        return obj.urlImage_wide.url

    def get_imagem_url(self, obj):
        return obj.urlImage_medium.url

    def get_imagen_url(self, obj):
        return obj.urlImage_wide.url