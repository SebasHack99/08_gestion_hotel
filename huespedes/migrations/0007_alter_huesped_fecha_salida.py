# Generated by Django 5.1.7 on 2025-04-20 17:59

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('huespedes', '0006_alter_huesped_fecha_salida'),
    ]

    operations = [
        migrations.AlterField(
            model_name='huesped',
            name='fecha_salida',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
