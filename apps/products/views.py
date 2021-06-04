from django.views.generic import TemplateView

from apps.products.models import Banner


class IndexView(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['banner'] = Banner.objects.first()

        return context


class ProductDetailView(TemplateView):
    template_name = 'pages/product_detail.html'