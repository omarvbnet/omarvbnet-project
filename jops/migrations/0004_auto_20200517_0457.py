# Generated by Django 3.0.6 on 2020-05-17 01:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jops', '0003_auto_20200517_0451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='job_date',
        ),
        migrations.RemoveField(
            model_name='job',
            name='url1',
        ),
    ]