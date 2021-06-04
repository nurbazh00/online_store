from django.db import models

from apps.products.models import Product
from apps.users.models import User


class Cart(models.Model):
    user = models.ForeignKey(to=User,
                             on_delete=models.SET_NULL,
                             related_name='user_carts',
                             null=True)


    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


    def __str__(self):
        return f'{self.user.email} - корзина: {self.id}'


class CartItem(models.Model):
    cart = models.ForeignKey(to=Cart, on_delete=models.CASCADE,
                             related_name='cart_items')
    product = models.ForeignKey(to=Product,
                                on_delete=models.SET_NULL,
                                related_name='product_cart_item',
                                null=True)
    quantity = models.SmallIntegerField(verbose_name='Количество')


    class Meta:
        verbose_name = 'Содержимое корзины'
        verbose_name_plural = 'Содержимое корзины'


    def __str__(self):
        return f'item: {self.id}, cart: {self.cart.id}'