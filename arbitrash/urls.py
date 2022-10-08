"""arbitrash URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from settings.views import index,changer, about_us, confirm
from users.views import register, user_login
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('imzhorobekov123/', admin.site.urls),
    path('', index, name="index"),
    path('exchange/', changer, name="changer"),
    path('about_us/', about_us, name="about_us"),
    path('confirm/', confirm, name="confirm"),
    path('register/', register, name="register"),
    path('login/', user_login, name="login"),
    path('logout/', LogoutView.as_view(next_page = 'index'), name = "logout"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)