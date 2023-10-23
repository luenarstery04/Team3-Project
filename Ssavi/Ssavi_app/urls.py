from django.urls import path
from . import views

urlpatterns = [
    path('', views.album_list, name='index'),
    path('', views.album_list, name='index'),
    path('detail/', views.detail, name='detail'),
    path('recommend/', views.recommend, name='recommend'),
    path('playlist/', views.playlist, name='playlist'),
    path('liked_album/', views.liked_album, name='liked_album'),
    path('liked_track/', views.liked_track, name='liked_track'),
    path('myInfo/', views.myInfo, name='myInfo'),
    path('delPlayList/<str:pk>', views.delPlayList, name='delete'),
]