from django.urls import path

# from apps.boards.views import DetailBoardView
from apps.orders.views import json_orders

app_name = 'orders'

urlpatterns = [
    path(
        'json',
        json_orders,
    ),
]