# Generated by Django 4.1.5 on 2023-07-07 17:44

from django.db import migrations, models
import xxx.models


class Migration(migrations.Migration):

    dependencies = [
        ('xxx', '0028_domain_siteimages'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteimages',
            name='thumb_compress',
            field=models.ImageField(blank=True, editable=False, upload_to=xxx.models.image_path),
        ),
        migrations.AlterField(
            model_name='siteimages',
            name='orig_img',
            field=models.ImageField(blank=True, editable=False, upload_to=xxx.models.image_path),
        ),
        migrations.AlterField(
            model_name='siteimages',
            name='thumb',
            field=models.ImageField(blank=True, editable=False, upload_to=xxx.models.image_path),
        ),
    ]
