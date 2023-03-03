# Generated by Django 4.1.7 on 2023-03-03 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_system', '0013_album_track'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='track',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='track',
            name='album',
        ),
        migrations.AddField(
            model_name='companyasset',
            name='slug',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='companyinventory',
            name='slug',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='employee',
            name='slug',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='employer',
            name='slug',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='timeoff',
            name='slug',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Track',
        ),
    ]
