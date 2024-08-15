# Generated by Django 5.1 on 2024-08-11 19:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieApp', '0004_alter_review_director'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='MovieApp.director'),
        ),
        migrations.AlterField(
            model_name='review',
            name='director',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_reviews', to='MovieApp.director'),
        ),
    ]
