from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """ Модель пользователя """

    phone = models.CharField(max_length=35, verbose_name='Номер телефона', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='Город', **NULLABLE)

    telegram_username = models.CharField(max_length=50, unique=True, verbose_name="Имя пользователя в ТГ")
    telegram_chat_id = models.CharField(max_length=50, default=0, unique=True, verbose_name="ID чата", **NULLABLE)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"