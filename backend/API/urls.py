from django.contrib import admin
from django.urls import path
from .views import uye_kayit , uye_listesi, suresi_biten_uyeler , suresi_yaklasan_uyeler , uye_detay , islem_gecmisi

urlpatterns = [
    path('uyeler-ekle/',uye_kayit, name='uye_kayit'),
    path('uye/<int:id>/',uye_detay, name='uye_detay'),
    path('',uye_listesi, name='uye_listesi'),
    path('suresi-biten-uye-liste/',suresi_biten_uyeler, name='suresi_biten_uyeler'),
    path('suresi-yaklasan-uye-liste/',suresi_yaklasan_uyeler, name='suresi_yaklasan_uyeler'),
    path('islem-gecmisi/',islem_gecmisi,name='islem_gecmisi')
]