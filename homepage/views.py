from typing import Any

from django.db.models import Count
from django.views.generic import TemplateView

from company.models import Company
from products.models import Product

from .models import Slide

# Create your views here.


class HomepageView(TemplateView):
    template_name = 'homepage/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = Company.objects.first()
        context['slides'] = Slide.objects.all()
        context['products'] = Product.objects.all()

        categories_with_counts = (
            Product.objects.values('category')
            .annotate(product_count=Count('category'))
            .filter(product_count__gt=0)
        )
        unique_category_names = {
            Product.objects.get(category=item['category']).get_category_display()
            for item in categories_with_counts
        }
        context['categories'] = unique_category_names
        return context
