# Generated by Django 3.0.6 on 2020-05-17 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jops', '0008_auto_20200517_0520'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='video',
            field=models.FileField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]
