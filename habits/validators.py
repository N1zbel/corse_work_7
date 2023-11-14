from rest_framework.exceptions import ValidationError


def choose_related_habit_or_reward(related_habit, reward):
    """ Исключения одновременного выбора связанной привычки и указания вознаграждения. """

    if related_habit and reward:
        raise ValidationError('Привычка должна быть либо со связанной привычкой, либо с награждением!')


def check_pleasant_habit_with_related_habit(related_habit):
    """ Проверки связанной привычки с признаком приятной привычки. """

    if related_habit and not related_habit.pleasant_habit:
        raise ValidationError('Связанная привычка должна быть приятной!')


def check_no_reward_or_related_habit_for_pleasant_habit(data):
    """ Проверки приятности привычки """

    pleasant_habit = data.get('pleasant_habit')
    reward = data.get('reward')
    related_habit = data.get('related_habit')

    if pleasant_habit and (reward or related_habit):
        raise ValidationError('У приятной привычки не должно быть вознаграждения')


class PeriodicityHabitValidator:
    """ Проверки периодичности привычки """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        periodicity = dict(value).get(self.field)
        if periodicity:
            if periodicity > 7 or periodicity == 0:
                raise ValidationError('Привычка должна выполняться не чем раз в семь дней')