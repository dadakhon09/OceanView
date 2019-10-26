from django.shortcuts import render
from django.views import View


class CarsView(View):
    def get(self, request):
        return render(request, 'cars.html', {})
