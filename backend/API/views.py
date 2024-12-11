from django.shortcuts import render, redirect , get_object_or_404
from .models import Kullanici , IslemGecmisi , MesajGecmisi
from django.utils.timezone import now
from django.http import HttpResponse
def uye_kayit(request):
      if request.method == 'POST':
            
            ad_soyad = request.POST.get('ad_soyad')
            uyelik_suresi = int(request.POST.get('uyelik_suresi_ay'))
            ucret = request.POST.get('ucret')
            tel_no = request.POST.get('tel_no')
            notlar = request.POST.get('notlar')

            yeni_uye = Kullanici(
                  ad_soyad=ad_soyad,
                  tel_no=tel_no,
                  ucret=ucret,
                  uyelik_suresi_ay=uyelik_suresi,
                  notlar=notlar)
            yeni_uye.save()
            
            IslemGecmisi.objects.create(
                  kullanici=yeni_uye,
                  islem_tipi="Yeni Üye Eklendi",
                  ucret = ucret
            )

            return redirect('uye_kayit')
      return render(request, 'uye_kayit.html')

def uye_listesi(request):
      uyeler = Kullanici.objects.all()
      return render(request, 'uye_listesi.html', {'uyeler':uyeler})

def suresi_biten_uyeler(request):
      tum_uyeler = Kullanici.objects.all()
      suresi_biten_uyeler = [uye for uye in tum_uyeler if uye.hesapla_kalan_gun == 0]
      return render(request, 'suresi_biten_uyeler.html', {'suresi_biten_uyeler': suresi_biten_uyeler})

def suresi_yaklasan_uyeler(request):
      tum_uyeler = Kullanici.objects.all()
      suresi_yaklasan_uyeler = [uye for uye in tum_uyeler if uye.hesapla_kalan_gun <= 3 and uye.hesapla_kalan_gun != 0]
      return render(request, 'suresi_yaklasan_uyeler.html', {'suresi_yaklasan_uyeler':suresi_yaklasan_uyeler})

def uye_detay(request, id):
      uye = get_object_or_404(Kullanici, id=id)
    
      if request.method == 'POST':
            ay = request.POST.get('sure')
            yeni_not = request.POST.get('notlar') 

            if ay:
                try:
                    ay = int(ay)
                    if ay > 0:
                        uye.uyelik_suresi_ay += ay
                        uye.save()
                        IslemGecmisi.objects.create(
                              kullanici=uye,
                              islem_tipi=f"Üyelik Süresi ' {ay} ' Uzatıldı",
                              ucret=uye.ucret
                        )
                except ValueError:
                    return HttpResponse("Geçersiz süre değeri.", status=400)

            if yeni_not:
                  uye.notlar = yeni_not
                  uye.save()
            else:
                  uye.notlar = ''
                  uye.save()
                

            return redirect('uye_detay', id=uye.id)
      return render(request, 'uye_detay.html', {'uye': uye})


def islem_gecmisi(request):
      islem_gecmisi = IslemGecmisi.objects.all()
      return render(request, 'islem_gecmisi.html',{'islem_gecmisi':islem_gecmisi})

from datetime import date, timedelta
import pywhatkit

def whatsapp_mesaj_gonder(telefon_numarasi, mesaj):
      try:
            su_an = now()
            saat = su_an.hour
            dakika = su_an.minute + 1
            pywhatkit.sendwhatmsg(telefon_numarasi, mesaj, saat, dakika)
            print(f"Mesaj gönderildi: {telefon_numarasi} -> {mesaj}")
      except Exception as e:
            print(f"Mesaj gönderilirken hata oluştu: {e}")
            
def uyelik_bildirimi_gonder():
      bugun = now().date()
      kullanicilar = Kullanici.objects.all()
      
      for kullanici in kullanicilar:
            bitis_tarihi = kullanici.baslangic_tarihi + timedelta(days=kullanici.uyelik_suresi_ay*31)
            kalan_gun = (bitis_tarihi - bugun).days
            
            if not kullanici.tel_no:
                  continue
            
            if kalan_gun == 7:
                  mesaj_turu = "3_gün_kaldi"
                  if not MesajGecmisi.objects.filter(kullanici=kullanici, mesaj_tarihi=bugun, mesaj_turu=mesaj_turu).exists():
                        mesaj = f"Merhaba {kullanici.ad_soyad}, üyeliğinizin bitmesine 3 gün kaldı. Klas-fitness"
                        whatsapp_mesaj_gonder(f"+90{kullanici.tel_no}",mesaj)
                        MesajGecmisi.objects.create(kullanici=kullanici,mesaj_tarihi=bugun, mesaj_turu=mesaj_turu)
            elif kalan_gun == 0:
                  mesaj_turu = "uyelik_bitti"
                  if not MesajGecmisi.objects.filter(kullanici=kullanici, mesaj_tarihi=bugun, mesaj_turu=mesaj_turu).exists():
                        mesaj = f"Merhaba {kullanici.ad_soyad}, üyeliğiniz bugün sona ermiştir. Lütfen sürenizi yenileyin."
                        whatsapp_mesaj_gonder(f"+90{kullanici.tel_no}", mesaj)
                        MesajGecmisi.objects.create(kullanici=kullanici, mesaj_tarihi=bugun, mesaj_turu=mesaj_turu)
                        