from django.urls import path
from . import views

urlpatterns = [
    path('', views.album_list, name='index'),
    path('detail/', views.detail, name='detail'),
    path('recommend/', views.recommend, name='recommend'),
    path('album_list/', views.album_list, name='album_list'),
]