# Generated by Django 2.1.7 on 2020-02-16 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobsapp', '0011_applicant1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicant1',
            name='user',
        ),
        migrations.DeleteModel(
            name='Applicant1',
        ),
    ]