# Generated by Django 5.1.2 on 2024-11-26 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paquete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('cantidadInventario', models.IntegerField()),
                ('PrecioVenta', models.IntegerField()),
                ('fechaCaducidad', models.DateField()),
            ],
        ),
    ]
