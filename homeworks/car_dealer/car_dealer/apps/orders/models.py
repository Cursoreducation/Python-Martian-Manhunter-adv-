from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Order(models.Model):
    card = models.ForeignKey(
        'cars.car',
        on_delete=models.CASCADE,
    )

    STATUS_ORDER_DONE = 'done'
    STATUS_ORDER_ACTIVE = 'active'
    STATUS_ORDER_REJECT = 'reject'

    STATUS_ORDER_CHOICES = (
        (STATUS_ORDER_DONE, 'Выполнено'),
        (STATUS_ORDER_ACTIVE, 'Выполняется'),
        (STATUS_ORDER_REJECT, 'Отменено'),
    )

    status_order = models.CharField(
        max_length=30,
        choices=STATUS_ORDER_CHOICES,
        default=STATUS_ORDER_ACTIVE,
    )

    first_name = models.CharField(
        max_length=50
    )

    second_name = models.CharField(
        max_length=50
    )

    email = models.EmailField(
        max_length=60,
    )

    phone = PhoneNumberField(
        unique=False,
        null=False,
        blank=False
    )

    message = models.TextField(
        blank=True,
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.first_name} {self.second_name}'