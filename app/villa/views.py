from django.shortcuts import render
from django.views import View


class VillasView(View):
    def get(self, request):
        return render(request, 'villas.html', {})
