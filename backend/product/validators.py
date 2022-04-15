from rest_framework.validators import UniqueValidator
from .models import Product


unique_validator = UniqueValidator(
    queryset=Product.objects.all(),
    lookup='iexact',
)