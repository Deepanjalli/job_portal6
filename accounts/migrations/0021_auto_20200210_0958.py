# Generated by Django 2.1.7 on 2020-02-10 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_auto_20200210_0950'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='hotel',
            managers=[
            ],
        ),
        migrations.RenameField(
            model_name='hotel',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='recruiter',
        ),
    ]
