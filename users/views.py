from django.shortcuts import render,redirect
from settings.models import Setting
from django.contrib.auth import login, authenticate
from .models import User
# Create your views here.
def register(request):
    setting = Setting.objects.latest('id')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            try:
                user = User.objects.create(username = username)
                user.set_password(password)
                user.save()
                user = User.objects.get(username = username)
                user = authenticate(username = username, password = password)
                login(request, user)
                return redirect('index')
            except:
                return redirect('register_error')
    context = {
        'setting' : setting,
    }
    return render(request, 'register.html', context)

def user_login(request):
    setting = Setting.objects.latest('id')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username = username)
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('index')
        except:
            return redirect('login')
    context = {
        'setting' : setting,
    }
    return render(request, 'sign_in.html', context)
