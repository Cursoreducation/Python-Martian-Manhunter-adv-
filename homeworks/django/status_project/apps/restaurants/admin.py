from django.contrib import admin

# Register your models here.
from apps.restaurants.models import Restaurant, RestaurantPerson, RestaurantCountry, RestaurantCity, RestaurantMenu, RestaurantDish

admin.site.register(Restaurant)
admin.site.register(RestaurantPerson)
admin.site.register(RestaurantCountry)
admin.site.register(RestaurantCity)
admin.site.register(RestaurantMenu)
admin.site.register(RestaurantDish)