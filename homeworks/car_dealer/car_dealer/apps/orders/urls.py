from django.urls import path

# from apps.boards.views import DetailBoardView
from apps.orders.views import OrdersListView, DetailOrderView

app_name = 'boards'

urlpatterns = [
    path(
        '',
        OrdersListView.as_view(),
    ),
    path(
        '<int:order_id>/',
        DetailOrderView.as_view(),
    ),
]