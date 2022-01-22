# Generated by Django 3.2.9 on 2022-01-22 19:41

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
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Purpose', models.CharField(max_length=50)),
                ('Propertytype', models.CharField(max_length=50)),
                ('City', models.CharField(max_length=50)),
                ('Location', models.CharField(max_length=255)),
                ('ZipCode', models.IntegerField()),
                ('PropertyTitle', models.CharField(max_length=50)),
                ('Description', models.CharField(blank=True, max_length=255)),
                ('Price', models.IntegerField()),
                ('LandArea', models.IntegerField()),
                ('Unit', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(blank=True, default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('UserName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]