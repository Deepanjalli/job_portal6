# Generated by Django 2.1.7 on 2020-02-16 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0043_auto_20200216_1128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='country',
        ),
        migrations.RemoveField(
            model_name='user',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='user',
            name='dob_city',
        ),
        migrations.RemoveField(
            model_name='user',
            name='dob_country',
        ),
        migrations.RemoveField(
            model_name='user',
            name='dob_state',
        ),
        migrations.RemoveField(
            model_name='user',
            name='experience',
        ),
        migrations.RemoveField(
            model_name='user',
            name='job_title',
        ),
        migrations.RemoveField(
            model_name='user',
            name='location',
        ),
        migrations.RemoveField(
            model_name='user',
            name='middle_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='mob',
        ),
        migrations.RemoveField(
            model_name='user',
            name='pin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='state',
        ),
        migrations.RemoveField(
            model_name='user',
            name='tel',
        ),
    ]
