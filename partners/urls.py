from django.urls import path
from . import views

urlpatterns = [
    path('opinions/', views.OpinionList.as_view() ),
]