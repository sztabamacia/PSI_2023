# Generated by Django 4.2.8 on 2023-12-04 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteka', '0004_ksiazka_osoba_alter_wypozyczenie_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ksiazka',
            old_name='osoba',
            new_name='owner',
        ),
    ]
