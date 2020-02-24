# Generated by Django 2.1.7 on 2020-02-08 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20200208_1048'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('hotel_Main_Img', models.FileField(upload_to='images/')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='avatar',
        ),
    ]
