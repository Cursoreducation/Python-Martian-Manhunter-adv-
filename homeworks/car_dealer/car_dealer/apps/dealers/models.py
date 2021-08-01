from django.contrib.auth import get_user_model
from django.db import models

USER_MODEL = get_user_model()
# Create your models here.

class Dealer(models.Model):
    title = models.CharField(max_length=150)
    email = models.EmailField(
        max_length=60,
        unique=True,
    )

    city = models.ForeignKey(
        'dealers.City',
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        USER_MODEL,
        on_delete=models.CASCADE,
        related_name='dealer',
    )

    class Meta:
        verbose_name = 'Дилер'
        verbose_name_plural = 'Дилера'

    def __str__(self):
        return self.title


class City(models.Model):
    name = models.CharField(
        max_length=70,
        unique=True,
    )
    country = models.ForeignKey(
        'dealers.country',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(
        max_length=70,
        unique=True,
    )
    code = models.CharField(
        max_length=5,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return self.name
