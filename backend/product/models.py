from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL

class Product(models.Model):
    
    user = models.ForeignKey(User,
                             default=1,
                             on_delete=models.SET_NULL,
                             related_name='products',
                             null=True)
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

