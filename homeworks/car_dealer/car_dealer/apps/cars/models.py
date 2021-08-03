from django.db import models


# Create your models here.


class Car(models.Model):
    color = models.ForeignKey(
        'cars.Color',
        on_delete=models.CASCADE,
    )

    dealer = models.ForeignKey(
        'dealers.Dealer',
        on_delete=models.CASCADE,
    )

    model = models.ForeignKey(
        'cars.Model',
        on_delete=models.CASCADE,
    )

    ENGINE_CARBURETOR = 'carburetor'
    ENGINE_INJECTOR = 'injector'
    ENGINE_ELECTRIC = 'electric'

    ENGINE_CHOICE = (
        (ENGINE_CARBURETOR, 'Carburetor'),
        (ENGINE_INJECTOR, 'Injector'),
        (ENGINE_ELECTRIC, 'Electric'),
    )

    engine_type = models.CharField(
        max_length=30,
        choices=ENGINE_CHOICE,
        default=ENGINE_CARBURETOR,
    )

    POPULATION_YOUTH = 'youth'
    POPULATION_FAMILY = 'family'
    POPULATION_SPORTSMAN = 'sportsman'
    POPULATION_TRAVELERS = 'travelers'
    POPULATION_ALL = 'all'

    POPULATION_CHOICE = (
        (POPULATION_YOUTH, 'Для молодежи'),
        (POPULATION_FAMILY,'Для семьи'),
        (POPULATION_SPORTSMAN,'Для спортсменов'),
        (POPULATION_TRAVELERS, 'Для путешественников'),
        (POPULATION_ALL, 'Для всех'),
    )

    population_type = models.CharField(
        max_length=30,
        choices=POPULATION_CHOICE,
        default=POPULATION_ALL,
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    # FUEL_ELECTRICITY = 'electricity'
    # FUEL_DIESEL = 'diesel'
    # FUEL_PETROL = 'petrol'
    # FUEL_GAS = 'gas'
    #
    # FUEL_CHOICE = (
    #     (FUEL_ELECTRICITY, 'Electricity'),
    #     (FUEL_DIESEL, 'Diesel'),
    #     (FUEL_PETROL, 'Petrol'),
    #     (FUEL_GAS, 'Gas'),
    # )
    #
    # fuel_type = models.CharField(
    #     max_length=30,
    #     choices=FUEL_CHOICE,
    #     default=FUEL_PETROL,
    # )

    fuel_type = models.ForeignKey(
        'cars.FuelType',
        on_delete=models.CASCADE,
    )

    STATUS_PENDING = 'pending'
    STATUS_PUBLISH = 'published'
    STATUS_SOLD = 'sold'
    STATUS_ARCHIVED = 'archived'

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending Car Sell"),
        (STATUS_PUBLISH, "Published"),
        (STATUS_SOLD, "Sold"),
        (STATUS_ARCHIVED, "Archived"),
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING,
    )

    doors = models.SmallIntegerField()

    capacity = models.DecimalField(
        max_digits=3,
        decimal_places=2,
    )

    GEAR_CASE_MECHANICAL = 'mechanical'
    GEAR_CASE_AUTOMATIC = 'automatic'
    GEAR_CASE_ROBOTIC = 'robotic'
    GEAR_CASE_VARIABLE = 'variable'

    GEAR_CASE_CHOICES = (
        (GEAR_CASE_MECHANICAL, "Mechanical"),
        (GEAR_CASE_AUTOMATIC, "Automatic"),
        (GEAR_CASE_ROBOTIC, "Robotic"),
        (GEAR_CASE_VARIABLE, "Variable"),
    )

    gear_case = models.CharField

    number = models.CharField(max_length=10)

    slug = models.SlugField(max_length=75)

    sitting_place = models.SmallIntegerField()

    first_registration_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
    )

    engine_power = models.SmallIntegerField()

    description = models.TextField(
        blank=True,
    )

    category = models.ManyToManyField(
        'cars.Property',
        blank=True,
    )

    pictures = models.ForeignKey(
        'cars.picture',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машини'

    def __str__(self):
        return self.slug


class Color(models.Model):
    name = models.CharField(max_length=70)

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    def __str__(self):
        return self.name


class Model(models.Model):
    brand = models.ForeignKey(
        'cars.Brand',
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=70)

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=70)

    logo = models.ImageField(
        upload_to='pictures_brand_logo',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.name


class Property(models.Model):
    CATEGORY_PASSENGER = 'passenger'
    CATEGORY_BUS = 'bus'
    CATEGORY_TRUCK = 'Truck'

    CATEGORY_CHOICES = (
        (CATEGORY_PASSENGER, 'Passenger car'),
        (CATEGORY_BUS, 'Bus'),
        (CATEGORY_TRUCK, 'Truck')
    )

    category = models.CharField(
        max_length=40,
        choices=CATEGORY_CHOICES,
        default=CATEGORY_PASSENGER,
    )

    name = models.CharField(max_length=155)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Picture(models.Model):
    url = models.ImageField(
        upload_to='pictures_car',
        null=True,
        blank=True,
    )

    position = models.SmallIntegerField(
        blank=True,
    )

    metadata = models.CharField(
        max_length=100,
        blank=True,
    )

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

    def __str__(self):
        return self.metadata


class FuelType(models.Model):
    FUEL_ELECTRICITY = 'electricity'
    FUEL_DIESEL = 'diesel'
    FUEL_PETROL = 'petrol'
    FUEL_GAS = 'gas'

    FUEL_CHOICE = (
        (FUEL_ELECTRICITY, 'Electricity'),
        (FUEL_DIESEL, 'Diesel'),
        (FUEL_PETROL, 'Petrol'),
        (FUEL_GAS, 'Gas'),
    )

    fuel_type = models.CharField(
        max_length=30,
        choices=FUEL_CHOICE,
        default=FUEL_PETROL,
        unique=True,
    )

    class Meta:
        verbose_name = 'Тип топлива'
        verbose_name_plural = 'Топливо'

    def __str__(self):
        return self.fuel_type