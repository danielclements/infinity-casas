# Generated by Django 3.0.8 on 2022-03-23 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='meal_type',
            new_name='currency',
        ),
        migrations.RemoveField(
            model_name='property',
            name='calories',
        ),
        migrations.RemoveField(
            model_name='property',
            name='ingredients',
        ),
        migrations.RemoveField(
            model_name='property',
            name='meal_img',
        ),
        migrations.RemoveField(
            model_name='property',
            name='name',
        ),
    ]
