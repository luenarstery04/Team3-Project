from django.shortcuts import render, redirect, get_object_or_404
from .models import Albums
from mysqlsearcher import *
from django.db.models import Q
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
    # 현재 all을 통해 모든 테이블 내용을 출력하려 하고 있다. 비효율적이다.
    # 유저의 인증정보를 조회하여 id값을 보낸다.
    # 제대로 작동하지 않는다. 고칠 게 많다.
    if request.user.is_authenticated:
        user_id = request.user.id
        user_genre_list = DBsearch.selectUserGenre(user_id)

        # 받아온 장르는 ['k-pop', 'jazz'] 이렇게 리스트로 온다
        filter_query = Q()
        for genre in user_genre_list:
            filter_query |= Q(album_genre__contains=genre)

        recom_albums = Albums.objects.filter(filter_query)

    else:
        recom_albums = Albums.objects.all()
    return render(request, 'Ssavi_app/recommend.html', {'recom_albums':recom_albums})

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