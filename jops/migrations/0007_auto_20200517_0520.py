# Generated by Django 3.0.6 on 2020-05-17 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jops', '0006_auto_20200517_0515'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='body',
        ),
        migrations.RemoveField(
            model_name='job',
            name='pub_date',
        ),
    ]
