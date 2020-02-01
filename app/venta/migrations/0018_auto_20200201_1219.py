# Generated by Django 2.2.4 on 2020-02-01 15:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('salonCorte', '0016_tratamiento'),
        ('venta', '0017_auto_20200131_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='tratamiento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='salonCorte.Tratamiento'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateField(default=datetime.date(2020, 2, 1)),
        ),
    ]