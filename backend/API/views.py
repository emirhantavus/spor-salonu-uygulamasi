from django.shortcuts import render, redirect , get_object_or_404
from .models import Kullanici
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
                except ValueError:
                    return HttpResponse("Geçersiz süre değeri.", status=400)

            if yeni_not:
                uye.notlar = yeni_not
                uye.save()

            return redirect('uye_detay', id=uye.id)
      return render(request, 'uye_detay.html', {'uye': uye})