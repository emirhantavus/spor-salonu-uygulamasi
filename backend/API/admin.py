from django.contrib import admin
from .models import Kullanici, IslemGecmisi , UyelikGecmisi

admin.site.register(Kullanici)
admin.site.register(IslemGecmisi)
admin.site.register(UyelikGecmisi)
