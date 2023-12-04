# Generated by Django 4.2.8 on 2023-12-04 11:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('biblioteka', '0003_wypozyczenie_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='ksiazka',
            name='osoba',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ksiazka', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='wypozyczenie',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wypozyczenie', to=settings.AUTH_USER_MODEL),
        ),
    ]