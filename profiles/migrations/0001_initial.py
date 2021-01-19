# Generated by Django 3.1.5 on 2021-01-14 10:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=10)),
                ('bankingDetails', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_banking_details', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addressLineOne', models.CharField(max_length=30)),
                ('addressLineTwo', models.CharField(max_length=30)),
                ('surburb', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=50)),
                ('province', models.CharField(max_length=30)),
                ('postal_code', models.CharField(max_length=4)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
        ),
    ]
