# Generated by Django 4.2.2 on 2023-08-03 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equ', '0029_useractivitylog'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='lab',
            field=models.ForeignKey(default='001', on_delete=django.db.models.deletion.CASCADE, to='equ.lab'),
        ),
        migrations.DeleteModel(
            name='UserLab',
        ),
    ]
