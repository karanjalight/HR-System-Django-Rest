# Generated by Django 4.1.7 on 2023-03-03 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_system', '0014_alter_track_unique_together_remove_track_album_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyasset',
            name='slug',
            field=models.CharField(blank=True, help_text='Enter You Company Full Names', max_length=100),
        ),
        migrations.AlterField(
            model_name='companyinventory',
            name='slug',
            field=models.CharField(blank=True, help_text='Enter You Company Full Names', max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='slug',
            field=models.CharField(blank=True, help_text='Enter You Company Full Names', max_length=100),
        ),
        migrations.AlterField(
            model_name='employer',
            name='slug',
            field=models.CharField(blank=True, help_text='Enter You Company Full Names', max_length=100),
        ),
        migrations.AlterField(
            model_name='timeoff',
            name='slug',
            field=models.CharField(blank=True, help_text='Enter You Company Full Names', max_length=100),
        ),
    ]
