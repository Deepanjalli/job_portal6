# Generated by Django 2.2 on 2020-02-23 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0049_auto_20200223_0658'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='experience',
            new_name='experience1',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='location',
            new_name='location1',
        ),
    ]
