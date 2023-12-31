# Generated by Django 4.1.5 on 2023-03-01 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('xxx', '0011_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='level',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='node',
            name='root',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='xxx.node'),
        ),
    ]
