from django.contrib import admin

# Register your models here.
from .models import Restaurant, Employee, Country, City, Menu, Dish

admin.site.register(Restaurant)
admin.site.register(Employee)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Menu)
admin.site.register(Dish)