from django.db import models
from goods.models import Products

from users.models import User


class CartQueryset(models.QuerySet):
    
    def total_price(self):
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Cart(models.Model):

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Kullanıcılar')
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='Ürün')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name= 'Stok')
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestap = models.DateTimeField(auto_now_add=True, verbose_name='Eklenen tarih')

    class Meta:
        db_table = 'cart'
        verbose_name = "Sepet"
        verbose_name_plural = "Sepet"

    objects = CartQueryset().as_manager()


    def products_price(self):
        return round(self.product.sell_price() * self.quantity,2)


    def __str__(self):
        return f'Sepet {self.user.username} | Ürün {self.product.name} | Stok {self.quantity}'



