from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.conf import settings
from django.db.models import Q 


User = settings.AUTH_USER_MODEL

class ProductQuerySet(models.QuerySet):

    def is_public(self):
        return self.filter(is_public=True)

    def search(self, query, user=None, public=True):
        lookup = Q(title__icontains=query) | Q(content__icontains=query)
        qs = self.filter(lookup)
        
        if user is not None:
            qs = qs.filter(user=user)

        if public:
            qs = qs.is_public()

        return qs

class ProductManager(models.Manager):

    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def search(self, query, user=None):
        qs = self.get_queryset().search(query, user=user)
        return qs


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

