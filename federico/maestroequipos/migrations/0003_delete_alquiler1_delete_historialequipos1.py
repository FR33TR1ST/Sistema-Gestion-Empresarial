# Generated by Django 4.2.7 on 2023-11-14 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maestroequipos', '0002_rename_historialequipos_alquiler1_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='alquiler1',
        ),
        migrations.DeleteModel(
            name='historialequipos1',
        ),
    ]
