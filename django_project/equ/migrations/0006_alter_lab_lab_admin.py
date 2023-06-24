# Generated by Django 4.2.2 on 2023-06-23 10:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('equ', '0005_remove_lab_equipments_lab_lab_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab',
            name='lab_admin',
            field=models.ForeignKey(limit_choices_to={'groups__name': 'admin'}, on_delete=django.db.models.deletion.CASCADE, related_name='lab_admin_of', to=settings.AUTH_USER_MODEL),
        ),
    ]
