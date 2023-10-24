from django.urls import path
from . import views

urlpatterns = [
    path('', views.album_list, name='index'),
    path('detail/', views.detail, name='detail'),
    path('recommend/', views.recommend, name='recommend'),
    
    path('music_recommend/', views.music_recommend, name='music_recommend'),
    path('like_track/', views.like_track, name='like_track'),
    path('like_album/', views.like_album, name='like_album'),
]