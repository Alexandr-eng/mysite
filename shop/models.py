from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f"{self.cat.name}"


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name


class Warehouse(models.Model):
    name = models.CharField(max_length=128)
    quantity = models.PositiveIntegerField()


class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField()
    warhouse_id = models.ForeignKey(Warehouse, related_name="products",
                                    on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.warhouse_id.name}, price: {self.price}"


