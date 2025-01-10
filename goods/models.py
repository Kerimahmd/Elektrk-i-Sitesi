from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Ürün İsmi')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'Kategori'
        verbose_name_plural = 'Kategoriler'

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=150,  verbose_name='Ürün İsmi')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Açıklama')
    image = models.ImageField(upload_to ='goods_images', blank=True, null=True, verbose_name='Fotoğraf')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Fiyat')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Stok')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Kategori')
    feature_name = models.CharField(max_length=150, null=True, verbose_name='Marka İsmi')
    features_slug = models.SlugField(max_length=200, blank=True, null=True, verbose_name='URL')
    color = models.CharField(max_length=150, null=True, verbose_name='Renk')
    model = models.CharField(max_length=150, null=True, verbose_name='Model')

    class Meta:
        db_table = 'product'
        verbose_name = 'Ürün'
        verbose_name_plural = 'Ürünler'
        ordering = ("id",)

    def __str__(self):
        return f'{self.name} Stok - {self.quantity}'
    

    def sell_price(self):
        return self.price



    