from django.contrib import admin
from django.urls import path
from .views import uye_kayit

urlpatterns = [
    path('uyeler/',uye_kayit, name='uye_kayit'),
]