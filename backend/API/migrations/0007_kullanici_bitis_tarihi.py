# Generated by Django 5.0 on 2024-12-17 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0006_alter_mesajgecmisi_mesaj_tarihi'),
    ]

    operations = [
        migrations.AddField(
            model_name='kullanici',
            name='bitis_tarihi',
            field=models.DateField(blank=True, null=True),
        ),
    ]
