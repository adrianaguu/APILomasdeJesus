from .models import Category, News
from .serializers import CategorySerializer, NewsSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from django.http import Http404

class CategoryList(APIView):
	def get(self, request, format=None):
		snippets = Category.objects.all()
		serializer = CategorySerializer(snippets, many=True)
		return Response(serializer.data)

class NewsList(APIView):
	def get(self, request, format=None):
		snippets = News.objects.order_by('-date')
		serializer = NewsSerializer(snippets, many=True)
		return Response(serializer.data)

class NewsListbyCategory(APIView):
    def get(self, request, pk, format=None):
        category = Category.objects.get(pk=pk)
        snippets = News.objects.filter(category=category)
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

class NewsFiler(APIView):
    def post(self, request, format=None):
        year = request.data["year"]
        month = request.data["month"]
        categories = request.data["categories"]
        text = request.data["text"]        

        if text != "":
            news=News.objects.filter(Q(title__unaccent__icontains=text) | Q(texto__unaccent__icontains=text))

        else:
            news = News.objects.all()

        if month != "":
            news = news.filter(date__month=month)

        if year != "":
            news = news.filter(date__year=year)

        if categories:
            news = news.filter(category__in= categories)

        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)

class NewsDetail(APIView):

    def get_object(self, pk):
        try:
            return News.objects.get(pk=pk)
        except News.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        news = self.get_object(pk)
        serializer = NewsSerializer(news)
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