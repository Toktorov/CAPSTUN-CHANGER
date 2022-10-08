from django.contrib import admin
from .models import Setting, Images, Statics, BTC
# Register your models here.
admin.site.register(Setting)
admin.site.register(Images)
admin.site.register(Statics)
admin.site.register(BTC)