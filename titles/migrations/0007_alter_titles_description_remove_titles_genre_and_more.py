# Generated by Django 4.1.7 on 2023-03-15 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genres', '0001_initial'),
        ('titles', '0006_remove_titles_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titles',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание произведения'),
        ),
        migrations.RemoveField(
            model_name='titles',
            name='genre',
        ),
        migrations.AlterField(
            model_name='titles',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Название произведения'),
        ),
        migrations.AlterField(
            model_name='titles',
            name='year',
            field=models.IntegerField(blank=True, null=True, verbose_name='Год выпуска'),
        ),
        migrations.AddField(
            model_name='titles',
            name='genre',
            field=models.ManyToManyField(blank=True, related_name='titles', to='genres.genres'),
        ),
    ]