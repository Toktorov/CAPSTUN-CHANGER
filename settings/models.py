from django.db import models
# Create your models here.
class Setting(models.Model):
    title = models.CharField(max_length = 50, verbose_name = 'Название сайта')
    wallet = models.CharField(max_length = 100, verbose_name = 'Кашёлёк')
    logo_site = models.ImageField(upload_to="logo/")
    decription = models.TextField()
    cript_1 = models.CharField(verbose_name = 'обьём1', max_length=50)
    cript_2 = models.CharField(verbose_name = 'обьём2', max_length=50)
    cript_3 = models.CharField(verbose_name = 'обьём3', max_length=50)
    rez_1 = models.CharField(verbose_name = 'резерв1', max_length=50)
    rez_2 = models.CharField(verbose_name = 'резерв2', max_length=50)
    rez_3 = models.CharField(verbose_name = 'резерв3', max_length=50)
    def __str__(self):
        return self.title
    class Meta():
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"
        
class Images(models.Model):
    logo1 = models.FileField(upload_to="logo/")
    logo2 = models.FileField(upload_to="logo/")
    logo3 = models.FileField(upload_to="logo/")
    logo4 = models.FileField(upload_to="logo/")
    
    def __str__(self):
        return "Logo"
    
class Statics(models.Model):
    title = models.CharField(max_length = 50, verbose_name = 'Статика')
    text = models.CharField(max_length = 50, verbose_name = 'Текст статистики')
    img = models.ImageField(upload_to = "stat/")
    
class BTC(models.Model):
    title = models.CharField(max_length = 50, verbose_name = 'Имя валюты')
    price = models.FloatField( verbose_name = 'Курс валюты')
    
    def __str__(self):
        return self.title
    