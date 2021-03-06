# Generated by Django 2.2.4 on 2019-10-09 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('salonCorte', '0002_color_tintura'),
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoPago', models.CharField(max_length=20)),
                ('fecha', models.DateField(blank=True, null=True)),
                ('total', models.FloatField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persona.Cliente')),
                ('corte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salonCorte.Corte')),
                ('peluquero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persona.Empleado')),
                ('tintura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salonCorte.Tintura')),
            ],
        ),
    ]
