from django.urls import path

from goods import views

app_name = 'goods'

urlpatterns = [
    path('search/', views.goods, name ='search'),
    path('urunler/', views.goods, name ='urunler'),
    path('urunler/<slug:product_slug>/', views.product, name='urun_detay'),
]