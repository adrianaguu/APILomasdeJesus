from .models import Category, News
from .serializers import CategorySerializer, NewsSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import Http404

class CategoryList(APIView):
	def get(self, request, format=None):
		snippets = Category.objects.all()
		serializer = CategorySerializer(snippets, many=True)
		return Response(serializer.data)

class NewsList(APIView):
	def get(self, request, format=None):
		snippets = News.objects.order_by('date')
		serializer = NewsSerializer(snippets, many=True)
		return Response(serializer.data)

class NewsLastThree(APIView):
    def get(self, request, format=None):
    	snippets = News.objects.order_by('date')[0:3]
    	serializer = NewsSerializer(snippets, many=True)
    	return Response(serializer.data)

class NewsFourMoreViews(APIView):
    def get(self, request, format=None):
    	snippets = News.objects.order_by('views')[0:4]
    	serializer = NewsSerializer(snippets, many=True)
    	return Response(serializer.data)

class NewsOrderByViews(APIView):
    def get(self, request, format=None):
    	snippets = News.objects.order_by('views')
    	serializer = NewsSerializer(snippets, many=True)
    	return Response(serializer.data)

class NewsByDate(APIView):
    def post(self, request, format=None):
    	year = request.data["year"]
    	month = request.data["month"]
    	news = News.objects.filter(date__gte = datetime.date(year, month, 1),date__lte = datetime.date(year, month+1 , 1) )
    	serializer = NewsSerializer(snippets, many=True)
    	return Response(serializer.data)

class NewsDetail(APIView):

    def get_object(self, pk):
        try:
            return News.objects.get(pk=pk)
        except News.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        news = self.get_object(pk)
        serializer = SnippetSerializer(news)
        news.views = news.views + 1
        news.save() 
        return Response(serializer.data)

"""
class ImageGalleryList(APIView):

	def get(self, request, format=None):
		galleries = Gallery.objects.all()
		imagels_gal = []
		for g in galleries:
			images = ImageGallery.objects.filter(gallery=g)
			serializer = ImageGallerySerializer(images, many=True)
			imagels_gal.append({'name':g.name,'images':serializer.data})

		return Response({'galleries':imagels_gal})
"""