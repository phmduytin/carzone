# Generated by Django 3.2.16 on 2022-12-11 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='inquiry',
            new_name='Contact',
        ),
    ]