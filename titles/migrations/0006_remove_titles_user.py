# Generated by Django 4.1.7 on 2023-03-15 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0005_titles_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='titles',
            name='user',
        ),
    ]