from django.shortcuts import render
from django.views import View

from app.models import Sight


class AdminSightsView(View):
    def get(self, request):
        sights = Sight.objects.all()

        return render(request, 'adminka/sights.html', {'sights': sights})
