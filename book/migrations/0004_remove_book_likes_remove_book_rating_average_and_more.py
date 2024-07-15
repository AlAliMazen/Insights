# Generated by Django 4.2.13 on 2024-07-15 13:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='book',
            name='rating_average',
        ),
        migrations.AddField(
            model_name='book',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)]),
        ),
    ]
