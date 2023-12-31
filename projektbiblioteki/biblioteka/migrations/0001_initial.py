# Generated by Django 4.2.8 on 2023-12-04 11:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('autorID', models.IntegerField(primary_key=True, serialize=False)),
                ('imie', models.CharField(max_length=100)),
                ('nazwisko', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Wypozyczenie',
            fields=[
                ('idWypozyczenia', models.IntegerField(primary_key=True, serialize=False)),
                ('dataWypozyczenia', models.DateField()),
                ('dataZwrotu', models.DateField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='biblioteka', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ksiazka',
            fields=[
                ('idKsiazki', models.IntegerField(primary_key=True, serialize=False)),
                ('tytul', models.CharField(default='', max_length=100)),
                ('rokWydania', models.IntegerField()),
                ('dostepnosc', models.BooleanField()),
                ('autorID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteka.autor')),
                ('wypozyczenie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteka.wypozyczenie')),
            ],
        ),
        migrations.CreateModel(
            name='Klient',
            fields=[
                ('idKlient', models.IntegerField(primary_key=True, serialize=False)),
                ('imie', models.CharField(default='', max_length=100)),
                ('nazwisko', models.CharField(default='', max_length=100)),
                ('adres', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('nrtel', models.IntegerField()),
                ('klient_wypozyczenie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='biblioteka.wypozyczenie')),
            ],
        ),
    ]
