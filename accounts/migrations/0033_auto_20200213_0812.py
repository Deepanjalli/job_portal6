# Generated by Django 2.1.7 on 2020-02-13 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0032_auto_20200212_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='recruiter',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
    ]