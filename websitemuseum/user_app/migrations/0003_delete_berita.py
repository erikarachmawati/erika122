# Generated by Django 4.2.1 on 2023-06-10 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0002_alter_berita_table'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Berita',
        ),
    ]