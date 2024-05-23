from typing import Any

from django.views.generic import TemplateView

from company.models import Company

from .models import Slide

# Create your views here.


class HomepageView(TemplateView):
    template_name = 'homepage/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = Company.objects.first()
        context['slides'] = Slide.objects.all()
        return context
