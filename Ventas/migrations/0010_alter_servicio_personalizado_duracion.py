# Generated by Django 3.2.9 on 2022-03-24 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ventas', '0009_alter_servicio_personalizado_duracion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio_personalizado',
            name='duracion',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
