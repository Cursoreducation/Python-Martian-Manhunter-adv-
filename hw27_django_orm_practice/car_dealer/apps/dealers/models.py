from django.contrib.auth import get_user_model
from django.db import models

USER_MODEL = get_user_model()


class Dealer(models.Model):
    title = models.CharField(
        max_length=100,
    )
    email = models.EmailField(
        max_length=80,
    )

    user = models.OneToOneField(
        USER_MODEL,
        on_delete=models.CASCADE,
    )
    city = models.ForeignKey(
        'dealers.City',
        on_delete=models.CASCADE,
        related_name='dealers',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Dealer'
        verbose_name_plural = 'Dealers'


class Country(models.Model):
    name = models.CharField(
        max_length=80,
        unique=True,
    )
    code = models.CharField(
        max_length=7,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'


class City(models.Model):
    name = models.CharField(
        max_length=80,
    )

    country = models.ForeignKey(
        'dealers.Country',
        on_delete=models.CASCADE,
        related_name='cities',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'


class NewsLetter(models.Model):
    email = models.EmailField(
        max_length=80,
    )

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'News Letter'
        verbose_name_plural = 'News Letters'
