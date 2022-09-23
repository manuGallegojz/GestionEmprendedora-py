# Generated by Django 4.1.1 on 2022-09-22 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('whatsapp', models.CharField(max_length=150)),
                ('instagram', models.CharField(max_length=200)),
                ('localidad', models.CharField(max_length=100)),
                ('negocio', models.CharField(max_length=100)),
                ('actividad', models.TextField()),
                ('necesidad', models.CharField(max_length=100)),
                ('juridiccion', models.CharField(max_length=100)),
                ('exportar', models.CharField(max_length=100)),
                ('dependencia', models.CharField(max_length=100)),
                ('precios', models.CharField(max_length=100)),
                ('expectativas', models.TextField()),
                ('comentarios', models.TextField()),
            ],
        ),
    ]