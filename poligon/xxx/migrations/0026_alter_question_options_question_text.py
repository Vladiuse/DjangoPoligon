# Generated by Django 4.1.5 on 2023-04-25 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xxx', '0025_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['-pk']},
        ),
        migrations.AddField(
            model_name='question',
            name='text',
            field=models.CharField(default='123:', max_length=50),
            preserve_default=False,
        ),
    ]