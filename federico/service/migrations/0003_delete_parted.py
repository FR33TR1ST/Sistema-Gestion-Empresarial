# Generated by Django 4.2.7 on 2023-11-14 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_parted_end_date_parted_start_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='parted',
        ),
    ]
