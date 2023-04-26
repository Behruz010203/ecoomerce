from django.contrib import admin

from app.models import Category, Seller, Product, Photo


# Register your models here.
@admin.register(Category)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Seller)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Photo)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class AuthorAdmin(admin.ModelAdmin):
    pass
