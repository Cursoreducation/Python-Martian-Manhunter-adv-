from django.urls import path

# from apps.boards.views import DetailBoardView
from apps.dealers.views import json_dealers

app_name = 'cars'

urlpatterns = [
    path(
        'json',
        json_dealers,
    ),
]