# Generated by Django 2.1.7 on 2020-02-10 09:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_hotel_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='role',
            field=models.CharField(default=django.utils.timezone.now, error_messages={'required': 'Role must be provided'}, max_length=12),
            preserve_default=False,
        ),
    ]
