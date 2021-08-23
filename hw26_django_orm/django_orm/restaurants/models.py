from django.db import models


class Restaurant(models.Model):
    title = models.CharField(max_length=100, null=False)
    phone_number = models.CharField(max_length=13)
    email = models.CharField(max_length=60)
    city = models.ForeignKey(
        'restaurants.City',
        on_delete=models.CASCADE,
    )
    employers = models.ManyToManyField(
        'restaurants.Employee'
    )
    menus = models.ManyToManyField(
        'restaurants.Menu'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurants'


class Employee(models.Model):
    JOB_TITLE_DIRECTOR = 'director'
    JOB_TITLE_CHEF = 'chef'
    JOB_TITLE_COOK = 'cook'
    JOB_TITLE_WAITER = 'waiter'
    JOB_TITLE_CLEANER = 'cleaner'

    JOB_CHOICES = (
        (JOB_TITLE_DIRECTOR, 'Restaurant Director'),
        (JOB_TITLE_CHEF, 'Restaurant Head Chef'),
        (JOB_TITLE_COOK, 'Restaurant Cook'),
        (JOB_TITLE_WAITER, 'Restaurant Waiter/Waitress'),
        (JOB_TITLE_CLEANER, 'Restaurant CLeaner'),
    )

    name = models.CharField(max_length=20, null=False)
    surname = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=13)
    job_title = models.CharField(
        max_length=100,
        choices=JOB_CHOICES,
        default=JOB_TITLE_CLEANER,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'


class Country(models.Model):
    title = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'


class City(models.Model):
    title = models.CharField(max_length=50, null=False)
    country = models.ForeignKey(
        'restaurants.Country',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'


class Dish(models.Model):
    title = models.CharField(max_length=100, null=False)
    weight = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Dish'
        verbose_name_plural = 'Dishes'


class Menu(models.Model):
    SEASON_WINTER = 'winter'
    SEASON_SUMMER = 'summer'

    SEASON_CHOICES = (
        (SEASON_WINTER, 'Winter menu'),
        (SEASON_SUMMER, 'Summer menu'),
    )

    title = models.CharField(max_length=100, null=False)
    season = models.CharField(
        max_length=10,
        choices=SEASON_CHOICES,
        default=SEASON_SUMMER,
        blank=True,
    )
    dishes = models.ManyToManyField(
        'restaurants.Dish'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Season'
        verbose_name_plural = 'Seasons'
