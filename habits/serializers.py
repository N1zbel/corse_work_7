from rest_framework import serializers

from habits.models import Habit
from habits.validators import choose_related_habit_or_reward, check_pleasant_habit_with_related_habit, \
    check_no_reward_or_related_habit_for_pleasant_habit, PeriodicityHabitValidator


class HabitSerializer(serializers.ModelSerializer):
    """ Сериализатор привычки """

    class Meta:
        model = Habit
        fields = '__all__'

        validators = [
            PeriodicityHabitValidator(field='periodicity'),
        ]

    def validate(self, data):
        choose_related_habit_or_reward(data.get('related_habit'), data.get('reward'))
        check_pleasant_habit_with_related_habit(data.get('related_habit'))
        check_no_reward_or_related_habit_for_pleasant_habit(data)
        return data
