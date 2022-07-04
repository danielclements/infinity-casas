# Generated by Django 3.0.8 on 2022-06-14 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properies', '0017_auto_20220602_1228'),
    ]

    operations = [
        migrations.CreateModel(
            name='feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Features',
            },
        ),
        migrations.AddField(
            model_name='property',
            name='features',
            field=models.ManyToManyField(blank=True, to='properies.feature'),
        ),
    ]