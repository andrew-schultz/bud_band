# Generated by Django 3.1.6 on 2021-02-11 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bud_band', '0003_spotifysongcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spotifysongcomment',
            name='text',
            field=models.TextField(),
        ),
    ]
