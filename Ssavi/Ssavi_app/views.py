from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from mysqlsearcher import *
from django.db.models import Q
from django.core import serializers
import spotipy
from mySpotipyID import cid, csecret
from spotipy.oauth2 import SpotifyClientCredentials
import json

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=csecret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Create your views here.
def index(request):
    # album_info = get_albuminfo()
    return render(request, 'Ssavi_app/index.html')

def detail(request):
    return render(request, 'Ssavi_app/detail.html')

def recommend(request):
    # 로그인하지 않은 채 그냥 들어간다면 장르는 except로 고정된다.
    # 유저의 인증정보를 조회하여 id값을 보낸다.
    # 
    if request.user.is_authenticated:
        user_id = request.user.id
        # user_genre_list = DBsearch.selectUserGenre(str(user_id))

        # user_id 정수를 받아오면 users_app_user에서 user_genre 검색
        try:
            current_login_user = UsersAppUser.objects.get(id=user_id)
            user_genre_list = current_login_user.user_genre.split(",")
        except UsersAppUser.DoesNotExist:
            user_genre_list = []

        # filter_query = Q()
        # for genre in user_genre_list:
        #     filter_query |= Q(album_genre__contains=genre)

        # recom_albums = Albums.objects.filter(filter_query)
        recom_albums = Albums.objects.all()

        return render(request, 'Ssavi_app/recommend.html', {'recom_albums':recom_albums, 'user_genre_list':user_genre_list})

    else:
        user_genre_list = ['jazz', 'latin', 'alternative', 'R&b']
        recom_albums = Albums.objects.all()
    return render(request, 'Ssavi_app/recommend.html', {'recom_albums':recom_albums, 'user_genre_list':user_genre_list})

def get_albuminfo():
    search_result = sp.new_releases(country='KR', limit=9)
    album_infos = []
    album_image_urls = []

    for re in search_result['albums']['items']:
        album_image_urls.append(re['name'])
        album_image_urls.append(re['artists'][0]['name'])
        album_image_urls.append(re['release_date'])
        for imagemedium in re['images']:
            if imagemedium.get('height') == 300:
                album_image_urls.append(imagemedium['url'])

    for i in range(0, len(album_image_urls), 4):
        album_info = {
            'albumname': album_image_urls[i],
            'artistname': album_image_urls[i+1],
            'releasedate': album_image_urls[i+2],
            'url': album_image_urls[i+3]
        }
        album_infos.append(album_info)

    return album_infos

def album_list(request):
    albums = Albums.objects.all()[:12]
    return render(request, 'Ssavi_app/index.html', {'albums': albums})

def playlist(request):
    playlists = PlayList.objects.all()
    return render(request, 'Ssavi_app/playlist.html', {"playlists":playlists})

def liked_album(request):
    liked_albums = LikedAlbum.objects.all()
    return render(request, 'Ssavi_app/liked_album.html',{'liked_albums':liked_albums})

def liked_track(request):
    return render(request, 'Ssavi_app/liked_track.html')

def myInfo(request):
    return render(request, 'Ssavi_app/myInfo.html')

def delPlayList(request, pk):
    data = PlayList.objects.get(id=pk)
    data.delete()
    return redirect('playlist')