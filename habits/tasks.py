from config.settings import TG_API_KEY
from habits.models import Habit
from habits.services import send_message_tg

from celery import shared_task


@shared_task
def check_user_habits_and_send():
    """ Отправка пользователю привычки """

    print('Работаем')

    habits = Habit.objects.all()

    for habit in habits:
        message = f'Внимание!' \
                  f'\n{habit}'
        params = {
            'chat_id': habit.owner.telegram_chat_id,
            'text': message
        }

        create_url_message_to_user = f'https://api.telegram.org/bot' \
                                     f'{TG_API_KEY}/sendMessage?'

        print(
            f'Выполняется отправка сообщения:'
            f'\nКому:{habit.owner.telegram_username}'
            f'\nСообщение: {message}'
            f'\nПоследнее напоминание: {habit.last_send}'
        )

        send_message_tg(habit, create_url_message_to_user, params)
