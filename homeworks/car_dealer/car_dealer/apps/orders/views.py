from django.shortcuts import render, get_object_or_404
from django.core import serializers
from django.views.generic import TemplateView, RedirectView, CreateView, DetailView, ListView


# Create your views here.
from apps.orders.models import Order


class OrdersListView(ListView):
    model = Order.objects.all()
    context_object_name = 'orders'
    template_name = 'orders/list.html'

    def get_queryset(self):
        return Order.objects.all()


class DetailOrderView(DetailView):
    model = Order
    pk_url_kwarg = 'order_id'
    template_name = 'orders/detail.html'
    context_object_name = 'order'


def json_orders(request):
    orders = serializers.serialize("json", Order.objects.all())
    return render(
        request,
        'orders/json.html',
        {'orders': orders}
    )
