# Generated by Django 5.0 on 2024-12-10 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kullanici',
            name='baslangic_tarihi',
            field=models.DateField(auto_now_add=True),
        ),
    ]
