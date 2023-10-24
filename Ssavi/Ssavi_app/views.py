from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.core.paginator import Paginator

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Create your views here.
def index(request):
    return render(request, 'Ssavi_app/index.html')

def detail(request):
    return render(request, 'Ssavi_app/detail.html')

def recommend(request):
    return render(request, 'Ssavi_app/recommend.html')

def album_list(request):
    page = int(request.GET.get('page', 1))
    albums_per_page = 15 # 페이지당 앨범 수
    albums = Albums.objects.all()
    paginator = Paginator(albums, albums_per_page)
    page_albums = paginator.get_page(page)
    return render(request, 'Ssavi_app/index.html', {'albums': page_albums})


def music_recommend(request):
    tracks = Tracks.objects.all()
    liketrack = []

    if request.user.is_authenticated:
        user_id = request.user.id
        for i in tracks:
            if LikedTrack.objects.filter(id=user_id, track_id=i.track_id).exists():
                liketrack.append(i.track_id)

    context = {
        'tracks': tracks,
        'liketrack' : liketrack
    }

    print(liketrack)
    return render(request, 'Ssavi_app/music_recommend.html', context)

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
            if current_login_user.user_genre is None:
                user_genre_list = []
            else:
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


def like_track(request):
    if request.method == 'POST':
        track_id = request.POST.get('track_id')
        id = request.POST.get('id')
      
        try:
            track_id = Tracks.objects.get(track_id=track_id)
            id = UsersAppUser.objects.get(id=id)
            

            liked_track, created = LikedTrack.objects.get_or_create(track=track_id, id=id)

            if created:
                message = "트랙 따봉"
            else:
                liked_track.delete()
                message = "트랙 따봉 해제"

            return JsonResponse({'message': message})
        except UsersAppUser.DoesNotExist:
            return JsonResponse({'error': '사용자가 존재하지 않습니다.'}, status=404)
        except Tracks.DoesNotExist:
            return JsonResponse({'error': '트랙이 존재하지 않습니다.'}, status=404)
        
