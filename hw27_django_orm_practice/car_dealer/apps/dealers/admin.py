from django.contrib import admin

# Register your models here.
from .models import Dealer, Country, City, NewsLetter

admin.site.register(Dealer)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(NewsLetter)