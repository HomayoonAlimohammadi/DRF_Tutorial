from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Product(models.Model):
    
    title = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)
    base_price = models.DecimalField(max_digits=15, decimal_places=2)
    discount = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(1.0)],
        default=0.2,
    )

    @property
    def sale_price(self):
        return float(self.base_price) * (1- self.discount)

