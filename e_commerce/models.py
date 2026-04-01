from django.db import models

# Create your models here.


# =============================================================
# EXAMPLE 2 — E-commerce Product
# Covers: DecimalField, IntegerField, ChoiceField,
#         ImageField, SerializerMethodField, FloatField
# =============================================================

# --- models.py ---
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    class ConditionChoices(models.TextChoices):
        NEW = 'new', 'New'
        USED = 'used', 'Used'
        REFURBISHED = 'refurbished', 'Refurbished'

    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.FloatField(default=0.0)     # e.g. 0.15 = 15% off
    stock = models.IntegerField(default=0)
    condition = models.CharField(
        max_length=15,
        choices=ConditionChoices.choices,
        default=ConditionChoices.NEW
    )
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name