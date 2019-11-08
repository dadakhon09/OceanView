from django.shortcuts import render
from django.views import View

from app.models import Sight


class SightsView(View):
    def get(self, request):
        sights = Sight.objects.all()

        return render(request, 'main/sights.html', {'sights': sights})
