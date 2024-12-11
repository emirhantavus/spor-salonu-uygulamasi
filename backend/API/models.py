from django.db import models
from datetime import timedelta , date
from django.utils.timezone import now

class Kullanici(models.Model):
      ad_soyad = models.CharField(max_length=255)
      baslangic_tarihi = models.DateField(default=date.today) # sonra değişecek. test amaclı böyle kaldı unutma.
      uyelik_suresi_ay = models.IntegerField()
      ucret = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
      tel_no = models.CharField(max_length=15, null=True, blank=True)
      notlar = models.TextField(null=True, blank=True)
      
      @property
      def hesapla_kalan_gun(self):
            bitis_tarihi = self.baslangic_tarihi + timedelta(days=self.uyelik_suresi_ay*31)
            kalan_gun = (bitis_tarihi - now().date()).days
            
            return max(kalan_gun, 0)
      
      def __str__(self):
            return f"{self.ad_soyad}  --  {self.hesapla_kalan_gun}"
      
class IslemGecmisi(models.Model):
      kullanici = models.ForeignKey(Kullanici, on_delete=models.CASCADE, related_name='islem_gecmisi')
      islem_tipi = models.CharField(max_length=255)
      tarih = models.DateField(auto_now_add=True)
      ucret = models.DecimalField(max_digits=10, decimal_places=2)
      
      def __str__(self):
            return f"{self.kullanici.ad_soyad}  --  {self.islem_tipi}"
      
class UyelikGecmisi(models.Model):
      kullanici = models.ForeignKey(Kullanici, on_delete=models.CASCADE, related_name='uyelik_gecmisi')
      ad_soyad = models.CharField(max_length=255)
      baslangic_tarihi = models.DateField()
      uyelik_suresi_ay = models.IntegerField()
      ucret = models.DecimalField(max_digits=10, decimal_places=2)
      tel_no = models.CharField(max_length=15, null=True, blank=True)

      def __str__(self):
          return f"{self.ad_soyad} - {self.baslangic_tarihi}"
