from django.shortcuts import render, get_object_or_404
from django.core import serializers
from django.views.generic import TemplateView, RedirectView, CreateView, DetailView, ListView


# Create your views here.
from apps.dealers.models import Dealer

from apps.cars.models import Car


class DealersListView(ListView):
    model = Dealer.objects.all()
    context_object_name = 'dealers'
    template_name = 'dealers/list.html'

    def get_queryset(self):
        return Dealer.objects.all()


def detail_dealer(request, dealer_id):
    dealer = get_object_or_404(Dealer,id=dealer_id)
    cars = Car.objects.filter(dealer_id=dealer_id)
    return render(
        request,
        'dealers/detail.html',
        {'dealer': dealer, 'cars': cars}
    )


def json_dealers(request):
    dealers = serializers.serialize("json", Dealer.objects.all())
    return render(
        request,
        'dealers/json.html',
        {'dealers': dealers}
    )
