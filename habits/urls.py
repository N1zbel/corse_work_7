from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitListAPIView, HabitCreateAPIView, HabitRetrieveAPIView, HabitUpdateAPIView, \
    HabitDestroyAPIView, PublicHabitListAPIView

app_name = HabitsConfig.name


urlpatterns = [
    path('habit/', HabitListAPIView.as_view(), name='habit_list'),
    path('habit_public/', PublicHabitListAPIView.as_view(), name='habit_public_list'),

    path('habit/create/', HabitCreateAPIView.as_view(), name='habit_create'),

    path('habit/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit_detail'),
    path('habit/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit_update'),

    path('habit/delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit_delete'),
]