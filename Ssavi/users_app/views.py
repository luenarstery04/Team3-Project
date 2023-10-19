from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .models import User
from .forms import UserForm

# Create your views here.

# 로그인 폼을 띄우고 로그인 진행한다
def sign_in(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            login(request, form.get_user())
            return redirect('index')
    else:
        form = AuthenticationForm()

    return render(request, 'users_app/sign_in.html', {'form':form})

def sign_out(request):
    logout(request)
    return redirect('index')

# 회원가입 폼을 띄우고 가입 진행한다
def sign_up(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user_name = request.POST['user_name']
        user_genre = ','.join(request.POST.getlist('genre_list'))

        user = User.objects.create_user(username, email, password)
        user.user_name = user_name
        user.user_genre = user_genre

        user.save()
        return redirect('sign_in')

    else:
        form = UserForm()

    return render(request, 'users_app/sign_up.html', {'form':form})