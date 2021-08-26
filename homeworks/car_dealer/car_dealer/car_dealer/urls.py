"""car_dealer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from rest_framework.authtoken.views import obtain_auth_token


def main_page(request):
    return render(
        request,
        'main/main-page.html',
    )


urlpatterns = [
    path(
        'admin/',
        admin.site.urls
    ),
    path(
        'cars/',
        include('apps.cars.urls')
    ),
    path(
        'dealers/',
        include('apps.dealers.urls')
    ),
    path(
        'orders/',
        include('apps.orders.urls')
    ),
    path(
        '',
        main_page,
    ),
    path(
        'api/car/',
        include('apps.cars.urls-api')
    ),
    path(
        'api/dealer/',
        include('apps.dealers.urls-api')
    ),
    path(
        'api/order/',
        include('apps.orders.urls-api')
    ),
    path(
        'subscribe/',
        include('apps.newsletter.urls')
    ),
    path(
        'api-token-auth/',
        obtain_auth_token
         ),
    path(
        'user/',
        include('apps.auth_token.urls')
         ),
]
