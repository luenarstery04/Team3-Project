from django.shortcuts import render, redirect, get_object_or_404
from .models import Albums
from django.template.loader import render_to_string  
from django.http import JsonResponse
from django.template import loader
from django.core.paginator import Paginator

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