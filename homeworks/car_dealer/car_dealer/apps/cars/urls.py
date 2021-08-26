from django.urls import path

# from apps.boards.views import DetailBoardView
from apps.cars.views import CarsView, detail_car

app_name = 'cars'

urlpatterns = [
    path(
        '',
        CarsView.as_view({'get': 'list'}),
    ),
    path(
        '<str:car_slug>/',
        detail_car,
    ),
]
