# Generated by Django 2.1.2 on 2018-10-18 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_coverphoto'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='poem',
            options={'ordering': ['name']},
        ),
    ]