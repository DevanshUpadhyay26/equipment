# Generated by Django 4.2.2 on 2023-06-23 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equ', '0013_alter_project_lab'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='lab',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipments', to='equ.lab'),
        ),
    ]
