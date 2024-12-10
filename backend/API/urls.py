from django.contrib import admin
from django.urls import path
from .views import uye_kayit , uye_listesi, suresi_biten_uyeler , suresi_yaklasan_uyeler

urlpatterns = [
    path('uyeler/',uye_kayit, name='uye_kayit'),
    path('uye-liste/',uye_listesi, name='uye_listesi'),
    path('suresi-biten-uye-liste/',suresi_biten_uyeler, name='suresi_biten_uyeler'),
    path('suresi-yaklasan-uye-liste/',suresi_yaklasan_uyeler, name='suresi_yaklasan_uyeler'),
]