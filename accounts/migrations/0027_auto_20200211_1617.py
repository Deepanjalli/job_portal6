# Generated by Django 2.1.7 on 2020-02-11 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0026_auto_20200211_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='hotel_Main_Img1',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]
