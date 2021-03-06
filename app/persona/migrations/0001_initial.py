# Generated by Django 2.2.4 on 2019-10-02 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=70)),
                ('apellidos', models.CharField(max_length=70)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=15)),
                ('direccion', models.CharField(max_length=70)),
                ('titulo', models.BooleanField()),
                ('persona', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='persona.Persona')),
            ],
            options={
                'verbose_name': 'Empleado ',
                'verbose_name_plural': 'Empleados',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vip', models.BooleanField()),
                ('persona', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='persona.Persona')),
            ],
            options={
                'verbose_name': 'Cliente ',
                'verbose_name_plural': 'Clientes',
                'ordering': ['id'],
            },
        ),
    ]
