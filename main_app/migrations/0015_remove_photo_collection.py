# Generated by Django 2.1.2 on 2018-10-18 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_photo_collection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='collection',
        ),
    ]
