from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
AUTH_USER_MODEL = get_user_model()


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    personal = models.ManyToManyField(
        'restaurants.RestaurantPerson'
    )
    country = models.OneToOneField(
        'restaurants.RestaurantCountry',
        on_delete=models.SET_NULL,
        null=True,
    )
    city = models.OneToOneField(
        'restaurants.RestaurantCity',
        on_delete=models.SET_NULL,
        null=True,
    )
    menu = models.ManyToManyField(
        'restaurants.RestaurantMenu'
    )

    class Meta:
        verbose_name = 'Ресторан'
        verbose_name_plural = 'Ресторани'


class RestaurantPerson(models.Model):
    POSITION_MANAGER = 'manager'
    POSITION_WAITER = 'waiter'
    POSITION_CLEANER = 'cleaner'
    POSITION_COOK = 'cook'

    POSITION_CHOICES = (
        (POSITION_MANAGER, "Manager"),
        (POSITION_WAITER, "Waiter"),
        (POSITION_CLEANER, "Cleaner"),
        (POSITION_COOK, "Cook"),
    )

    name = models.CharField(max_length=75)
    position = models.CharField(
        max_length=15,
        choices=POSITION_CHOICES,
        blank=True,
    )

    class Meta:
        verbose_name = 'Персонал'
        verbose_name_plural = 'Персонал'



class RestaurantCountry(models.Model):
    country = models.CharField(max_length=75)

    class Meta:
        verbose_name = 'Країна'
        verbose_name_plural = 'Країни'



class RestaurantCity(models.Model):
    city = models.CharField(max_length=75)

    class Meta:
        verbose_name = 'Місто'
        verbose_name_plural = 'Міста'


class RestaurantMenu(models.Model):
    name = models.CharField(max_length=60)
    dish = models.ManyToManyField(
        'restaurants.RestaurantDish'
    )

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class RestaurantDish(models.Model):
    dish = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Страва'
        verbose_name_plural = 'Страви'