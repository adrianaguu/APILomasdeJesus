from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.GalleryListCreate.as_view() ),
    path('list/images', views.ImageGalleryList.as_view() ),
]