# Generated by Django 2.1.7 on 2020-02-16 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0042_auto_20200216_1031'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='city',
            new_name='experience',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='tot_exp_mon',
            new_name='location',
        ),
        migrations.RemoveField(
            model_name='user',
            name='tot_exp_yr',
        ),
    ]
