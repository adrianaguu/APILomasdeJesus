from rest_framework import serializers
from .models import Opinion

class OpinionSerializer(serializers.ModelSerializer):
    partner_photo = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = Opinion
        fields = '__all__'

    def get_image_url(self, obj):
        return obj.partner_photo.url