# Generated by Django 2.2.4 on 2019-10-30 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'ordering': ['persona__apellidos'], 'verbose_name': 'Cliente ', 'verbose_name_plural': 'Clientes'},
        ),
    ]
