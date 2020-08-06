# Generated by Django 3.0.6 on 2020-08-05 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Galería',
                'verbose_name_plural': 'Galerías',
            },
        ),
        migrations.CreateModel(
            name='ImageGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=150, null=True, verbose_name='Descripción')),
                ('urlImage', models.ImageField(upload_to='images/galleries/', verbose_name='Imagen')),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='galleries.Gallery', verbose_name='Galería')),
            ],
            options={
                'verbose_name': 'Imagen',
                'verbose_name_plural': 'Imágenes',
            },
        ),
    ]
