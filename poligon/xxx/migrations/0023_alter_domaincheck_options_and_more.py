# Generated by Django 4.1.5 on 2023-03-16 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xxx', '0022_alter_domaincheck_check_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='domaincheck',
            options={'ordering': ['-is_checked', 'pk']},
        ),
        migrations.RenameField(
            model_name='domaincheck',
            old_name='id_checked',
            new_name='is_checked',
        ),
    ]
