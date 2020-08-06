# Generated by Django 3.0.6 on 2020-08-06 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('harga', models.FloatField(default=0)),
                ('stok', models.PositiveSmallIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Distributor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DetailSupplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.PositiveSmallIntegerField(default=0)),
                ('barang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gudang.Barang')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gudang.Supplier')),
            ],
        ),
        migrations.CreateModel(
            name='DetailDistributor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.PositiveSmallIntegerField(default=0)),
                ('barang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gudang.Barang')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gudang.Supplier')),
            ],
        ),
    ]