from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics

class OpinionList(generics.ListCreateAPIView):
    queryset = Opinion.objects.all()
    serializer_class = OpinionSerializer
