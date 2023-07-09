# Generated by Django 4.1.5 on 2023-03-01 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('xxx', '0010_delete_city_remove_country_langs_delete_people_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=10)),
                ('root', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='xxx.node')),
            ],
        ),
    ]