# Generated by Django 3.0.8 on 2022-04-25 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properies', '0008_property_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='self'),
        ),
    ]
