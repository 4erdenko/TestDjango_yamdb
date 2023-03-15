from django.db import models
from django.contrib.auth.models import AbstractUser
# from .validators import CustomUserValidation


class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        USER = "user", 'user'
        MODERATOR = "moderator", 'moderator',
        ADMIN = "admin", 'admin'

    base_role = Role.USER

    role = models.CharField(max_length=50, choices=Role.choices)

    username = models.CharField(
        'Username',
        # validators=(CustomUserValidation(),),
        unique=True,
        max_length=200
    )

    email = models.EmailField(
        'email',
        max_length=50,
        unique=True,
    )

    bio = models.TextField(
        'bio',
        max_length=300,
        blank=True
    )

    confirmation_code = models.CharField(
        'code',
        max_length=100,
        null=True
    )

    REQUIRED_FIELDS = ('email', )

    class Meta:
        ordering = ['id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return str(self.username)