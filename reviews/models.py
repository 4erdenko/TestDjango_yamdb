from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator

from django.db import models
from users.models import CustomUser
from titles.models import Titles

SCORE_CHOICES = [(i, i) for i in range(1, 11)]


class Review(models.Model):
    text = models.TextField(max_length=1000)
    author = models.ForeignKey(CustomUser,
                               on_delete=models.CASCADE,
                               related_name='reviews')
    score = models.IntegerField(choices=SCORE_CHOICES,
                                validators=[MinValueValidator(1),
                                            MaxValueValidator(10)])

    pub_date = models.DateTimeField(auto_now_add=True)
    title = models.ForeignKey(Titles,
                              on_delete=models.CASCADE,
                              related_name='reviews')

    class Meta:
        ordering = ['id']
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        unique_together = ('author', 'title')

    def save(self, *args, **kwargs):
        if not self.pk and self.author.reviews.filter(
                title=self.title).exists():
            raise ValidationError(f'Вы уже оставили отзыв на {self.title}')
        super().save(*args, **kwargs)
        self.title.title_score = self.title.reviews.aggregate(
            models.Avg('score'))['score__avg']
        self.title.save(update_fields=['title_score'])

    def __str__(self):
        return self.text
