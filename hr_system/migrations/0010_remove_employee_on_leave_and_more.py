# Generated by Django 4.1.7 on 2023-03-03 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr_system', '0009_alter_employee_employer_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='on_leave',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='time_off_end',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='time_off_start',
        ),
    ]
