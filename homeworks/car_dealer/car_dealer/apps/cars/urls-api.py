from django.urls import path

# from apps.boards.views import DetailBoardView
from apps.cars.views import json_cars

app_name = 'car'

urlpatterns = [
    path(
        'json',
        json_cars,
    ),
]