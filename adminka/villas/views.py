from django.shortcuts import render
from django.views import View

from app.models import Villa


class AdminVillasView(View):
    def get(self, request):
        villas = Villa.objects.all()

        return render(request, 'adminka/villas.html', {'villas': villas})
