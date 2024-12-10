from django.contrib import admin
from django.urls import path
from .views import uye_kayit , uye_listesi

urlpatterns = [
    path('uyeler/',uye_kayit, name='uye_kayit'),
    path('uye-liste/',uye_listesi, name='uye_listesi'),
]