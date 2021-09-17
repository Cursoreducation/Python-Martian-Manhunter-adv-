from django.contrib import admin
from django.urls import path

from .views import status, random_unicorn

urlpatterns = [
    path('admin/', admin.site.urls),
    path('status/', status, name='status'),
    path('runic', random_unicorn, name='random_color')
]
