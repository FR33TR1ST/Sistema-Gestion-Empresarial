# Generated by Django 4.2.7 on 2023-11-07 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='alquiler',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('equipo', models.CharField(default=None, max_length=512)),
                ('marcamodelo', models.CharField(default=None, max_length=512)),
                ('dominio', models.CharField(default=None, max_length=512, null=True)),
                ('propietario', models.CharField(default=None, max_length=512)),
                ('emplazamiento', models.CharField(default=None, max_length=512, null=True)),
                ('chofer', models.CharField(default=None, max_length=512, null=True)),
                ('valorpesos', models.IntegerField(default=0)),
                ('valordolares', models.IntegerField(default=0)),
                ('orden', models.CharField(default=None, max_length=512, null=True)),
                ('informacion', models.CharField(default=None, max_length=512, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='historialequipos',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('tipovehiculo', models.CharField(default=None, max_length=512, null=True)),
                ('numerointerno', models.CharField(default=None, max_length=512, null=True)),
                ('marca', models.CharField(default=None, max_length=512, null=True)),
                ('modelo', models.CharField(default=None, max_length=512, null=True)),
                ('dominio', models.CharField(default=None, max_length=512, null=True)),
            ],
        ),
    ]