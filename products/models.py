from django.db import models
# Create your models here.

class Brand(models.Model):
    brand_name = models.CharField(max_length=30)

    def __str__(self):
        return self.brand_name

class Model(models.Model):
    model_name = models.CharField(max_length=50)
    model_year = models.DateField(max_length=50)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.model_name

class Category(models.Model):
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.category_name

class Variant(models.Model):
    variant_name = models.CharField(max_length=50)

    def __str__(self):
        return self.variant_name

class Accessories(models.Model):
    accessory_name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.accessory_name

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