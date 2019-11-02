from django.shortcuts import render
from django.views import View

from app.models import Tour


class AdminToursView(View):
    def get(self, request):
        tours = Tour.objects.all()

        return render(request, 'adminka/tours.html', {'tours': tours})


class ToursCreateView(View):
    def get(self, request):
        return render(request, 'adminka/tours_create.html', {})
