# Generated by Django 4.1.7 on 2023-03-03 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr_system', '0015_alter_companyasset_slug_alter_companyinventory_slug_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyasset',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='companyinventory',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='employer',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='timeoff',
            name='slug',
        ),
    ]
