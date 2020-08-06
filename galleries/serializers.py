from rest_framework import serializers
from .models import Gallery, ImageGallery

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'

class ImageGallerySerializer(serializers.ModelSerializer):
    urlImage = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = ImageGallery
        exclude = ['gallery']

    def get_image_url(self, obj):
        return obj.urlImage.url