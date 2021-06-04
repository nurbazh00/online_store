from django.urls import path

from apps.products.views import IndexView, ProductDetailView


urlpatterns = [
    path('', IndexView.as_view(), name='index_page'),
    path('products/<int:pk>',
         ProductDetailView.as_view(), name='product_detail'),
]