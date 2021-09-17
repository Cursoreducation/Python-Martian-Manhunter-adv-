from django.db import models


class Car(models.Model):
    ENGINE_TYPE_HEAT = 'internal combustion'
    ENGINE_TYPE_HYBRID = 'hybrid'
    ENGINE_TYPE_ELECTRIC = 'electric'

    ENGINE_CHOICES = (
        (ENGINE_TYPE_HEAT, 'Internal combustion engine'),
        (ENGINE_TYPE_HYBRID, 'Hybrid engine'),
        (ENGINE_TYPE_ELECTRIC, 'Electric engine'),
    )

    engine = models.CharField(
        max_length=50,
        choices=ENGINE_CHOICES,
        default=ENGINE_TYPE_HEAT,
        blank=True
    )

    POLLUTANT_TYPE_A_PLUS = 'a+'
    POLLUTANT_TYPE_A = 'a'
    POLLUTANT_TYPE_B = 'b'
    POLLUTANT_TYPE_C = 'c'
    POLLUTANT_TYPE_D = 'd'
    POLLUTANT_TYPE_E = 'e'
    POLLUTANT_TYPE_F = 'f'
    POLLUTANT_TYPE_G = 'g'

    POLLUTANT_CHOICES = (
        (POLLUTANT_TYPE_A_PLUS, 'A+'),
        (POLLUTANT_TYPE_A, 'A'),
        (POLLUTANT_TYPE_B, 'B'),
        (POLLUTANT_TYPE_C, 'C'),
        (POLLUTANT_TYPE_D, 'D'),
        (POLLUTANT_TYPE_E, 'E'),
        (POLLUTANT_TYPE_F, 'F'),
        (POLLUTANT_TYPE_G, 'G'),
    )

    pollutant_choice = models.CharField(
        max_length=100,
        choices=POLLUTANT_CHOICES,
        default=POLLUTANT_TYPE_A,
    )

    STATUS_ACTIVE = 'active'
    STATUS_SOLD = 'sold'
    STATUS_ARCHIVED = 'archived'

    STATUS_CHOICES = (
        (STATUS_ACTIVE, 'Active'),
        (STATUS_SOLD, 'Sold'),
        (STATUS_ARCHIVED, 'Archived'),
    )

    car_status = models.CharField(
        max_length=100,
        choices=STATUS_CHOICES,
        default=STATUS_ACTIVE,
    )

    GEAR_MANUAL = 'manual'
    GEAR_SEMI = 'semi-automatic'
    GEAR_AUTOMATIC = 'automatic'

    GEAR_CHOICES = (
        (GEAR_MANUAL, 'Manual gear'),
        (GEAR_SEMI, 'Semi-automatic gear'),
        (GEAR_AUTOMATIC, 'Automatic gear'),
    )

    price = models.DecimalField(max_digits=9, decimal_places=2, default=50000)
    doors = models.PositiveSmallIntegerField(default=4)
    capacity = models.DecimalField(max_digits=3, decimal_places=2, default=1.5)

    gear_case = models.CharField(
        max_length=20,
        choices=GEAR_CHOICES,
        default=GEAR_MANUAL,
    )

    number = models.CharField(max_length=10)
    slug = models.SlugField(max_length=80)
    sitting_place = models.PositiveSmallIntegerField(default=4)
    first_registration_date = models.DateTimeField(auto_now_add=True)
    engine_power = models.PositiveSmallIntegerField()
    fuel_type = models.ForeignKey(
        'cars.FuelType',
        on_delete=models.CASCADE,
        related_name='cars',
    )

    dealer = models.ForeignKey(
        'dealers.Dealer',
        on_delete=models.CASCADE,
        related_name='cars',
    )

    picture = models.ForeignKey(
        'Picture',
        on_delete=models.CASCADE,
        related_name='cars',
    )

    color = models.ForeignKey(
        'Color',
        on_delete=models.CASCADE,
        related_name='cars',
    )

    model = models.ForeignKey(
        'Model',
        on_delete=models.CASCADE,
        related_name='cars'
    )

    property = models.ManyToManyField(
        'Property'
    )

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'


class Picture(models.Model):
    position = models.IntegerField()
    metadata = models.TextField(
        null=True,
        blank=True,
    )
    url = models.ImageField(
        upload_to='pictures',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.url.name

    class Meta:
        verbose_name = 'Picture'
        verbose_name_plural = 'Pictures'


class Color(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'


class Brand(models.Model):
    name = models.CharField(
        max_length=80,
        unique=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'


class Model(models.Model):
    name = models.CharField(
        max_length=80,
        unique=True,
    )

    brand = models.ForeignKey(
        'cars.Brand',
        on_delete=models.CASCADE,
        related_name='models',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Model'
        verbose_name_plural = 'Models'


class Property(models.Model):
    CATEGORY_SMALL = 'small'
    CATEGORY_MID = 'mid'
    CATEGORY_LARGE = 'large'
    CATEGORY_LUX = 'lux'
    CATEGORY_SPORT = 'sport'

    CATEGORY_CHOICES = (
        (CATEGORY_SMALL, "Small"),
        (CATEGORY_MID, "Midsize"),
        (CATEGORY_LARGE, "Large"),
        (CATEGORY_LUX, 'Luxury'),
        (CATEGORY_SPORT, "Sports")
    )

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default=CATEGORY_MID,
    )
    name = models.CharField(
        max_length=80,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'


class FuelType(models.Model):
    FUEL_GASOLINE = 'gasoline'
    FUEL_DIESEL = 'diesel'
    FUEL_ELECTRICITY = 'electricity'

    FUEL_CHOICES = (
        (FUEL_GASOLINE, 'Gasoline fuel'),
        (FUEL_DIESEL, 'Diesel fuel'),
        (FUEL_ELECTRICITY, 'Electricity fuel'),
    )

    fuel_type = models.CharField(
        max_length=100,
        choices=FUEL_CHOICES,
        default=FUEL_GASOLINE,
        unique=True,
    )

    def __str__(self):
        return self.fuel_type

    class Meta:
        verbose_name = 'Fuel type'
        verbose_name_plural = 'Fuel types'
