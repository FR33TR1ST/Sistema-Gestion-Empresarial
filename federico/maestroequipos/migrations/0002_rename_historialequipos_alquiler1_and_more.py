# Generated by Django 4.2.7 on 2023-11-08 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maestroequipos', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='historialequipos',
            new_name='alquiler1',
        ),
        migrations.RenameModel(
            old_name='alquiler',
            new_name='historialequipos1',
        ),
    ]
