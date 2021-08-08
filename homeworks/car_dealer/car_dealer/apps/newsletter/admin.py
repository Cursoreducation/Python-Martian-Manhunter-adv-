from django.contrib import admin

# Register your models here.
from apps.newsletter.models import Subscribers


admin.site.register(Subscribers)
