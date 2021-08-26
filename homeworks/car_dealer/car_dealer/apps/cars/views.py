from django.shortcuts import render, get_object_or_404
from django.core import serializers
from django.views.generic import TemplateView, RedirectView, CreateView, DetailView, ListView
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

# Create your views here.
from apps.cars.models import Car

from apps.cars.serializer import CarSerializer




class CarsView(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['model__name', 'model__brand__name', 'dealer__id']


    def list(self, request):
        return render(
            request,
            'cars/list.html',
            {
                'cars': self.filter_queryset(self.get_queryset()),
            }
        )



# class CarsListView(ListView):
#     model = Car.objects.all()
#     context_object_name = 'cars'
#     template_name = 'cars/list.html'
#
#     def get_queryset(self):
#         return Car.objects.all()


def detail_car(request, car_slug):
    car = get_object_or_404(Car, slug=car_slug)
    return render(
        request,
        'cars/detail.html',
        {'car': car}
    )


def json_cars(request):
    cars = serializers.serialize("json", Car.objects.all())
    return render(
        request,
        'cars/json.html',
        {'cars': cars}
    )
