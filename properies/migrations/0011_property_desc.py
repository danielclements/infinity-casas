# Generated by Django 3.0.8 on 2022-05-04 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properies', '0010_auto_20220425_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='desc',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]