from django.db import models
# Create your models here.

class Category(models.Model):
    PHONE = 'P'
    LAPTOP = 'L'
    DESKTOP = 'D'
    WATCH = 'W'

    CATEGORY_CHOICES = [
        (PHONE, 'Phone'),
        (LAPTOP, 'Laptop'),
        (DESKTOP, 'Desktop'),
        (WATCH, 'Watch'),
    ]

    category_name = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    category_image = models.ImageField()

class Manufacturer(models.Model):
    APPLE = 'APL'
    SAMSUNG = 'SAM'
    HAUWEI = 'HAU'
    NOKIA = 'NOK'
    SONY = 'SON'

    MANUFACTURER_CHOICES = [
        (APPLE, 'Apple'),
        (SAMSUNG, 'Samsung'),
        (HAUWEI, 'Hauwei'),
        (NOKIA, 'Nokia'),
        (SONY, 'Sony'),
    ]

    manufacturer_name = models.CharField(max_length=50, choices=MANUFACTURER_CHOICES, default=APPLE)

class ProductVariant(models.Model):
    RED = 'R'
    GREEN = 'G'
    BLUE = 'B'
    GREY = 'GR'
    BLACK = 'BL'

    VARIANT_CHOICES = [
        (RED, 'Red'),
        (GREEN, 'Green'),
        (BLUE, 'Blue'),
        (GREY, 'Grey'),
        (BLACK, 'Black')
    ]

    variant_type = models.CharField(max_length=20, choices=VARIANT_CHOICES, default=RED)

class Product(models.Model):
    SEALED_IN_BOX = 'SB'
    EXCELLENT = 'EX'
    FAIR = 'FA'
    DAMAGED = 'DA'

    CONDITION_CHOICES = [
        (SEALED_IN_BOX, 'Sealed In Box'),
        (EXCELLENT, 'Excellent'),
        (FAIR, 'Fair'),
        (DAMAGED, 'Damaged'),
    ]

    product_name = models.CharField(max_length=100)
    product_year = models.CharField(max_length=4)
    product_model = models.CharField(max_length=40)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    product_condition = models.CharField(max_length=2, choices=CONDITION_CHOICES, default=SEALED_IN_BOX)
    product_type = models.CharField(max_length=50)
    product_expected_price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)