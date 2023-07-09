# Generated by Django 4.1.5 on 2023-02-25 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xxx', '0007_people_delete_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iso', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iso', models.CharField(max_length=2)),
                ('langs', models.ManyToManyField(blank=True, to='xxx.lang')),
            ],
        ),
    ]