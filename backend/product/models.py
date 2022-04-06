from django.db import models


class Product(models.Model):
    
    title = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)

    @property
    def sale_price(self):
        return float(self.price) * 0.8

