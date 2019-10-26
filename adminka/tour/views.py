from django.shortcuts import render
from django.views import View

from app.models import Tour


class ToursView(View):
    def get(self, request):
        tours = Tour.objects.all()

        return render(request, 'tours.html', {'tours': tours})

