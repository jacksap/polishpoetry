# Generated by Django 2.1.2 on 2018-10-15 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20181015_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(max_length=500, verbose_name='Comment'),
        ),
    ]