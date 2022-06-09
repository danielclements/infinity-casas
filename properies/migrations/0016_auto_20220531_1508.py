# Generated by Django 3.0.8 on 2022-05-31 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('properies', '0015_auto_20220517_1147'),
    ]

    operations = [
        migrations.CreateModel(
            name='property_status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='property',
            name='secret_key',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='sold',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='properies.property_status'),
        ),
    ]