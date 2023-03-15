from django.db import models


class Genres(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название жанра')
    slug = models.SlugField(unique=True, verbose_name='Слаг')

    class Meta:
        ordering = ['id']
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name
