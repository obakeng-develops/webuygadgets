from django.db import models
# Create your models here.

class Brand(models.Model):
    brand_name = models.CharField(max_length=30)

class Model(models.Model):
    model_name = models.CharField(max_length=50)
    model_year= models.DateField(max_length=50)

class Category(models.Model):

    LAPTOP = 'LPTP'
    DESKTOP = 'DSKT'
    PHONE = 'PHNE'
    WATCH = 'WTCH'
    TABLET = 'TBLT'

    CATEGORY_CHOICES = [
        (LAPTOP, 'Laptop'),
        (DESKTOP, 'Desktop'),
        (PHONE, 'Phone'),
        (WATCH, 'Watch'),
        (TABLET, 'Tablet'),
    ]

    category_name = models.CharField(max_length=4, choices=CATEGORY_CHOICES, default=LAPTOP)

class Variant(models.Model):
    variant_name = models.CharField(max_length=50)

class Accessories(models.Model):
    accessory_name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Product(models.Model):

    SEALED_IN_BOX = 'SIB'
    EXCELLENT = 'EXC'
    FAIR = 'FIR'
    DAMAGED = 'DMG'

    CONDITION_CHOICES = [
        (SEALED_IN_BOX, 'Sealed In Box'),
        (EXCELLENT, 'Excellent'),
        (FAIR, 'Fair'),
        (DAMAGED, 'Damaged'),
    ]


    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    condition = models.CharField(max_length=3, choices=CONDITION_CHOICES, default=SEALED_IN_BOX)
    accessory = models.ForeignKey(Accessories, on_delete=models.CASCADE)