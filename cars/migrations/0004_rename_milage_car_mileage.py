# Generated by Django 3.2.16 on 2022-11-29 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_auto_20221129_0542'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='milage',
            new_name='mileage',
        ),
    ]
