# Generated by Django 5.0.1 on 2024-02-15 02:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carmodel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carmodel',
            name='car_brand_name',
        ),
    ]