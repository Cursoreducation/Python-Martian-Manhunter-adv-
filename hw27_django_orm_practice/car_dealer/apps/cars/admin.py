from django.contrib import admin

# Register your models here.
from .models import Car, Picture, Color, Brand, Model, Property

admin.site.register(Car)
admin.site.register(Picture)
admin.site.register(Color)
admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Property)