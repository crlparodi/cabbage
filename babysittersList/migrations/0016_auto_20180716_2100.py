# Generated by Django 2.0.7 on 2018-07-16 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('babysittersList', '0015_auto_20180716_1850'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=' ', max_length=42, verbose_name='Nom')),
                ('age', models.PositiveSmallIntegerField(default=0, verbose_name='Âge')),
                ('birth_location', models.CharField(default=' ', max_length=64, verbose_name='Lieu de naissance')),
                ('job', models.CharField(blank=True, choices=[('MF', 'Mère au Foyer')], max_length=4, verbose_name='Profession')),
            ],
        ),
        migrations.RemoveField(
            model_name='babysitter',
            name='age',
        ),
        migrations.RemoveField(
            model_name='babysitter',
            name='birth_location',
        ),
        migrations.RemoveField(
            model_name='babysitter',
            name='id',
        ),
        migrations.RemoveField(
            model_name='babysitter',
            name='job',
        ),
        migrations.RemoveField(
            model_name='babysitter',
            name='name',
        ),
        migrations.AddField(
            model_name='babysitter',
            name='user_link',
            field=models.OneToOneField(default=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='babysittersList.User'),
        ),
    ]