# Generated by Django 2.1.7 on 2020-02-14 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0038_auto_20200214_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='recruiter',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]