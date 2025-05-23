# Generated by Django 5.1.7 on 2025-03-31 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('estado', models.CharField(choices=[('disponible', 'Disponible'), ('reservada', 'Reservada'), ('mantenimiento', 'Mantenimiento')], default='disponible', max_length=20)),
                ('capacidad', models.IntegerField()),
                ('tipo', models.CharField(choices=[('familiar', 'Familiar'), ('pareja', 'Pareja')], default='familiar', max_length=20)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
