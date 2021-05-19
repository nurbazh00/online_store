from django.urls import path

from apps.products.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index_page'),
]