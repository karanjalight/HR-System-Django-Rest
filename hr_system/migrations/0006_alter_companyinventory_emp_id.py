# Generated by Django 4.1.7 on 2023-03-01 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr_system', '0005_rename_employer_id_companyinventory_emp_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyinventory',
            name='emp_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr_system.employer'),
        ),
    ]
