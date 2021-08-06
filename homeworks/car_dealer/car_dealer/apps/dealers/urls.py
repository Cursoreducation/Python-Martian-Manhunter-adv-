from django.urls import path

# from apps.boards.views import DetailBoardView
from apps.dealers.views import DealersListView, detail_dealer

app_name = 'dealers'

urlpatterns = [
    path(
        '',
        DealersListView.as_view(),
    ),
    path(
        '<int:dealer_id>/',
        detail_dealer,
    ),
]