from django.contrib import admin

from apps.products.models import Category, Product, Picture, Rating, Comment,\
    Banner


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Picture)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['image']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'category']


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['star', 'product', 'user']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'product', 'user']


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['title']




