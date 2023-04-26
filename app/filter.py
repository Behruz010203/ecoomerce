import django_filters
from django_filters import rest_framework

from app.models import Product


class ProductFilter(rest_framework.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')

    class Meta:
        model = Product
        fields = ('name', 'price')
