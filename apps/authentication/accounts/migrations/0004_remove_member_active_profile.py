# Generated by Django 2.2.2 on 2019-06-19 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190615_1144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accounts',
            name='active_profile',
        ),
    ]