# Generated by Django 2.2 on 2020-02-21 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0045_auto_20200216_1402'),
        ('jobsapp', '0012_auto_20200216_1402'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(default='', max_length=40)),
                ('experience', models.CharField(default='', max_length=40)),
                ('dob_city', models.CharField(default='', max_length=40)),
                ('dob_state', models.CharField(default='', max_length=40)),
                ('dob_country', models.CharField(default='', max_length=40)),
                ('dob', models.CharField(default='', max_length=40)),
                ('address', models.CharField(default='', max_length=40)),
                ('location', models.CharField(default='', max_length=40)),
                ('state', models.CharField(default='', max_length=40)),
                ('country', models.CharField(default='', max_length=40)),
                ('pin', models.CharField(default='', max_length=40)),
                ('tel', models.CharField(default='', max_length=40)),
                ('mob', models.CharField(default='', max_length=40)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.User')),
            ],
        ),
    ]
