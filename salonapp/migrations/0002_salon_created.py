# Generated by Django 4.1.7 on 2023-03-08 07:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('salonapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='salon',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
