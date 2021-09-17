from django.db import models


class Order(models.Model):
    STATUS_OPEN = 'open'
    STATUS_IN_PROGRESS = 'in progress'
    STATUS_COMPLETED = 'completed'
    STATUS_CANCELLED = 'cancelled'

    STATUS_CHOICES = (
        (STATUS_OPEN, 'Open'),
        (STATUS_IN_PROGRESS, 'In progress'),
        (STATUS_COMPLETED, 'Completed'),
        (STATUS_CANCELLED, 'Cancelled')
    )

    status = models.CharField(
        max_length=100,
        choices=STATUS_CHOICES,
        default=STATUS_OPEN,
        blank=True
    )

    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    message = models.TextField()

    car = models.ForeignKey(
        'cars.Car',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
