from django.db import models
from rest_framework.exceptions import ValidationError

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    """ Модель привычки """

    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)

    place = models.CharField(max_length=100, verbose_name='Место')
    time = models.TimeField(verbose_name='Время')
    action = models.TextField(verbose_name='Действие')
    periodicity = models.PositiveIntegerField(default=1, verbose_name='Периодичность выполнения')
    time_to_complete = models.IntegerField(verbose_name='Время на выполнение, в секундах')

    pleasant_habit = models.BooleanField(default=False, verbose_name='Признак приятной привычки')
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='Связанная привычка', **NULLABLE)

    reward = models.TextField(verbose_name='Вознаграждение за выполнение действия', **NULLABLE)

    is_public = models.BooleanField(default=False, verbose_name='Признак публичности привычки')

    last_send = models.DateTimeField(verbose_name='Последняя отправка напоминания', **NULLABLE)

    def __str__(self):
        if self.reward:
            reward = self.reward
        elif self.related_habit:
            reward = self.related_habit.action
        else:
            reward = 'то - что ты пожелаешь'
        return f'Я буду делать {self.action} в {self.time}, ' \
               f'\nместо: {self.place}' \
               f'\nНаграда: {reward}'

    def save(self, *args, **kwargs):
        """ Проверка выполнения привычки"""

        if self.time_to_complete and self.time_to_complete > 120:
            raise ValidationError('Время выполнения привычки должно быть больше 0 и меньше 120 секунд!')
        return super().save(**kwargs)

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
        ordering = ('pk',)
