# Generated by Django 4.0.6 on 2022-09-01 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('identificacion', models.BigIntegerField(unique=True, verbose_name='# de identificación')),
                ('telefono', models.IntegerField(verbose_name='Teléfono')),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=50, verbose_name='Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('identificacion', models.IntegerField(unique=True, verbose_name='# de identificación')),
                ('telefono', models.IntegerField(verbose_name='Teléfono')),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=8, verbose_name='Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificacion', models.IntegerField(unique=True, verbose_name='# de documento')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellido')),
                ('correo', models.EmailField(max_length=50, unique=True, verbose_name='Correo')),
                ('telefono', models.IntegerField(verbose_name='Teléfono')),
                ('rol', models.CharField(choices=[('Administrador', 'Administrador'), ('Vendedor', 'Vendedor')], max_length=50, verbose_name='Rol')),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=50, verbose_name='Estado')),
            ],
            options={
                'db_table': 'persona_usuario',
            },
        ),
    ]
