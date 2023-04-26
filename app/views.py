from django_filters import rest_framework
from rest_framework import viewsets

from app.filter import ProductFilter
from app.models import Category, Product
from app.serializers import CategorySerializer, SellerSerializer, ProductSerializer


class CategoryReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer


class SellerReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = SellerSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filterset_fields = ('name', 'price')
