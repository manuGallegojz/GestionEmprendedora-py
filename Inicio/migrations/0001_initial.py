# Generated by Django 4.1.1 on 2022-09-22 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.URLField()),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('instagram', models.URLField()),
                ('linkedin', models.URLField()),
            ],
        ),
    ]
