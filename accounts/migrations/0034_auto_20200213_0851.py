# Generated by Django 2.1.7 on 2020-02-13 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0033_auto_20200213_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('vendor', 'Vendor'), ('employer', 'Employer')], default='', max_length=10, null=True),
        ),
    ]