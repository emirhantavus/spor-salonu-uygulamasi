from django.contrib import admin
from .models import Kullanici, IslemGecmisi , UyelikGecmisi

class KullaniciAdmin(admin.ModelAdmin):
    list_display = ('id', 'ad_soyad', 'baslangic_tarihi', 'uyelik_suresi_ay')
    fields = ('ad_soyad', 'baslangic_tarihi', 'uyelik_suresi_ay', 'notlar')

admin.site.register(Kullanici, KullaniciAdmin)  
admin.site.register(IslemGecmisi)
admin.site.register(UyelikGecmisi)
