# Generated by Django 4.1.5 on 2023-02-20 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xxx', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='man',
            name='lang',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='Language',
        ),
        migrations.DeleteModel(
            name='Man',
        ),
    ]
