# Generated by Django 2.1.7 on 2020-02-12 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0031_auto_20200212_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='recruiter',
            field=models.CharField(blank=True, choices=[('vendor', 'Vendor'), ('employer', 'Employer')], default='', max_length=10, null=True),
        ),
    ]
