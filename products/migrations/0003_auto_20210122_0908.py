# Generated by Django 3.1.5 on 2021-01-22 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210121_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brand_name',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='model',
            name='model_name',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
