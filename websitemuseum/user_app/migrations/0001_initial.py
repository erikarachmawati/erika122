# Generated by Django 4.2.1 on 2023-06-03 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Berita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=255)),
                ('deskripsi', models.TextField()),
                ('tanggal', models.DateField()),
                ('gambar', models.ImageField(upload_to='berita_images/')),
            ],
        ),
    ]
