# Generated by Django 4.0.2 on 2022-07-08 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='driver',
            options={'ordering': ['id'], 'verbose_name': 'driver', 'verbose_name_plural': 'drivers'},
        ),
    ]
