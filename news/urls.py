from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryList.as_view() ),
    path('list/', views.NewsList.as_view() ),
    path('last_three/', views.NewsLastThree.as_view() ),
    path('four_more_views/', views.NewsFourMoreViews.as_view() ),
    path('filter/', views.NewsFiler.as_view() ),
    path('detail/<int:pk>', views.NewsDetail.as_view() ),
    path('list/by_category/<int:pk>',views.NewsListbyCategory.as_view())
]