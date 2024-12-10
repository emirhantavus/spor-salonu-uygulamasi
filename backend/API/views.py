from django.shortcuts import render, redirect
from .models import Kullanici
from django.utils.timezone import now

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