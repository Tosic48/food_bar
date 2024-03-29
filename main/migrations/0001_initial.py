# Generated by Django 4.1.7 on 2023-03-14 19:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Сakes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('layer_number', models.PositiveIntegerField()),
                ('vegetarion_type', models.CharField(choices=[('vegeterian', 'For Vegeterian'), ('non_vegeterian', ' No Vegeterian')], max_length=14)),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
    ]
