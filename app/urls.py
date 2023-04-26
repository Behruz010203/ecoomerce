from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from app.views import CategoryReadOnlyViewSet, SellerReadOnlyViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register(r'category', CategoryReadOnlyViewSet)
router.register(r'seller', SellerReadOnlyViewSet)
router.register(r'product', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
