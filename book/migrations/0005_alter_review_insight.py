# Generated by Django 4.2.13 on 2024-07-15 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_remove_book_likes_remove_book_rating_average_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='insight',
            field=models.TextField(),
        ),
    ]
