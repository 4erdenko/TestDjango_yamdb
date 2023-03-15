# Generated by Django 4.1.7 on 2023-03-14 20:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0003_alter_titles_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titles',
            name='title_score',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
    ]