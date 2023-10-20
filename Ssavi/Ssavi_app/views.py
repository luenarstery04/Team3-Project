from django.shortcuts import render, redirect, get_object_or_404
from .models import Albums

# Create your views here.
def index(request):
    return render(request, 'Ssavi_app/index.html')

def detail(request):
    return render(request, 'Ssavi_app/detail.html')

def recommend(request):
    return render(request, 'Ssavi_app/recommend.html')

# 콘텐츠
def album_list(request):
    albums = Albums.objects.all()[:12]
    return render(request, 'Ssavi_app/index.html', {'albums': albums})