from rest_framework import serializers
from .models import Gallery, ImageGallery

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'

class ImageGallerySerializer(serializers.ModelSerializer):
    urlImage = serializers.SerializerMethodField('get_image_url')
    urlImage_small = serializers.SerializerMethodField('get_image_urls')

    class Meta:
        model = ImageGallery
        exclude = ['gallery']

    def get_image_url(self, obj):
        return obj.urlImage.url

    def get_image_urls(self, obj):
        return obj.urlImage_small.url