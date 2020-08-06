from .models import Gallery, ImageGallery
from .serializers import GallerySerializer, ImageGallerySerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

class GalleryListCreate(generics.ListCreateAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

class ImageGalleryList(APIView):

	def get(self, request, format=None):
		galleries = Gallery.objects.all()
		imagels_gal = []
		for g in galleries:
			images = ImageGallery.objects.filter(gallery=g)
			serializer = ImageGallerySerializer(images, many=True)
			imagels_gal.append({'name':g.name,'images':serializer.data})

		return Response({'galleries':imagels_gal})




