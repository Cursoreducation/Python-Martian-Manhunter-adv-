from django.urls import path

# from apps.boards.views import DetailBoardView
from apps.cars.views import CarsListView, detail_car

app_name = 'cars'

urlpatterns = [
    path(
        '',
        CarsListView.as_view(),
    ),
    path(
        '<str:car_slug>/',
        detail_car,
    ),
]