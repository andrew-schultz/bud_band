# Generated by Django 3.1.7 on 2021-03-08 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bud_band', '0008_auto_20210308_0520'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
    ]
