# Generated by Django 4.1.5 on 2023-02-20 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xxx', '0004_city_position_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='position',
        ),
        migrations.RemoveField(
            model_name='position',
            name='city',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='Position',
        ),
    ]
