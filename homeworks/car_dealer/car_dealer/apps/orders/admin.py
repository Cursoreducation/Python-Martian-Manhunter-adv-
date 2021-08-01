from django.contrib import admin

# Register your models here.
from apps.orders.models import Order


class TaskAdmin(admin.ModelAdmin):
    list_display = ('model_id', 'dealer_id')


admin.site.register(Order)
