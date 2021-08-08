from django.db import models

# Create your models here.


class Subscribers(models.Model):
    email = models.EmailField(
        max_length=60,
        unique=True,
    )

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'

    def __str__(self):
        return self.email
