from django.shortcuts import render
from django.views import View

from app.models import Villa


class VillasView(View):
    def get(self, request):
        villas = Villa.objects.all()

        return render(request, 'main/villas.html', {'villas': villas})


class VillaView(View):
    def get(self, request, id):
        

        return render(request, 'main/villa_view.html', {})
