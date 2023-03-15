from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from categories.models import Category
from genres.models import Genres
from users.models import CustomUser


class Titles(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='Название произведения')
    description = models.TextField(verbose_name='Описание произведения',
                                   blank=True, null=True)
    genre = models.ManyToManyField(Genres, related_name='titles', blank=True)
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 related_name='titles',
                                 null=True,verbose_name='Категория')
    title_score = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name='Рейтинг',)
    year = models.IntegerField(verbose_name='Год выпуска', blank=True,
                               null=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name
