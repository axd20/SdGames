# Generated by Django 5.0.9 on 2024-11-10 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPrincipal', '0011_alter_producto_descripcion_alter_producto_nombre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='direccion',
            field=models.CharField(max_length=120),
        ),
    ]
