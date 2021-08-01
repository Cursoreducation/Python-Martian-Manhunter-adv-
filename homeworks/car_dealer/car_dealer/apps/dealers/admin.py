from django.contrib import admin

# Register your models here.
from apps.dealers.models import Dealer, City, Country


class TaskAdmin(admin.ModelAdmin):
    list_display = ('model_id', 'dealer_id')


admin.site.register(Dealer)
admin.site.register(City)
admin.site.register(Country)

