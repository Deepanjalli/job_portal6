# Generated by Django 2.1.7 on 2020-02-12 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0030_auto_20200211_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='recruiter',
            field=models.BooleanField(blank=True, default='', max_length=10, null=True),
        ),
    ]
