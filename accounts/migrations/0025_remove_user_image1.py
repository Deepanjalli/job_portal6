# Generated by Django 2.1.7 on 2020-02-10 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_auto_20200210_1034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='image1',
        ),
    ]
