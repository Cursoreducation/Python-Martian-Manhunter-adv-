from django.contrib import admin

# Register your models here.
from apps.cars.models import Car, Brand, Model, Color, Property, Picture, FuelType


admin.site.register(Car)
admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Color)
admin.site.register(Property)
admin.site.register(Picture)
admin.site.register(FuelType)
