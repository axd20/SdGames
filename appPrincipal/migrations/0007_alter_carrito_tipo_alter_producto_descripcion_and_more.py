# Generated by Django 5.0.9 on 2024-11-10 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPrincipal', '0006_alter_carrito_tipo_alter_venta_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrito',
            name='tipo',
            field=models.CharField(blank=True, choices=[('E', 'En Proceso'), ('C', 'Completado')], default='E', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='reclamo',
            name='descripcion',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='direccion',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='venta',
            name='estado',
            field=models.CharField(blank=True, default='Pendiente', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='venta',
            name='total',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
