# Generated by Django 2.2.4 on 2019-10-25 01:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
        ('venta', '0006_auto_20191024_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='tipoPago',
            field=models.CharField(blank=True, choices=[('Efectivo', 'Efectivo'), ('Debito', 'Débito'), ('Credito', 'Crédito'), ('Cuenta', 'Cta. Corriente')], max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='Sueldo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_empleado', models.CharField(blank=True, choices=[('Peluquero', 'Peluquero'), ('Ayudante', 'Ayudante')], max_length=50, null=True)),
                ('pago_semanal', models.FloatField(blank=True, null=True)),
                ('sueldo_basico', models.FloatField(blank=True, null=True)),
                ('adelanto', models.FloatField(blank=True, null=True)),
                ('peluquero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persona.Empleado')),
            ],
        ),
    ]
