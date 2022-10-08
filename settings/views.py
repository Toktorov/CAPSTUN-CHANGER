from django.shortcuts import render
from .models import Setting, Images, Statics, BTC
# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    images = Images.objects.latest('id')
    statics = Statics.objects.all()
    context = {
        "setting": setting,
        "images" : images,
        "statics": statics
    }
    return render(request, "index.html", context)

def changer(request):
    setting = Setting.objects.latest('id')
    btc = BTC.objects.all()
    context = {
        "setting": setting,
        'btc': btc
    }
    return render(request, "exchange.html", context)

def about_us(request):
    setting = Setting.objects.latest("id")
    context = {
        'setting': setting
    }
    return render(request, "about_us.html", context)

def confirm(request):
    setting = Setting.objects.latest("id")
    context = {
        'setting': setting
    }
    return render(request, "confirm.html", context)
