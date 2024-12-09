from django.db import models


class Kullanici(models.Model):
      ad_soyad = models.CharField(max_length=255)
      baslangic_tarihi = models.DateField()
      uyelik_suresi_ay = models.IntegerField()
      ucret = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
      tel_no = models.CharField(max_length=15, null=True, blank=True)
      notlar = models.TextField(null=True, blank=True)
      
      def __str__(self):
            return self.ad_soyad
      
class IslemGecmisi(models.Model):
      kullanici = models.ForeignKey(Kullanici, on_delete=models.CASCADE, related_name='islem_gecmisi')
      islem_tipi = models.CharField(max_length=255)
      tarih = models.DateField()
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