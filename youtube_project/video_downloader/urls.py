from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name = 'home'),
    path('search_results/', views.search, name='search'),
    path('download_page/', views.download_page, name='download_page'),
]