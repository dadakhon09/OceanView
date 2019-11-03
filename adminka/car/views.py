from django.shortcuts import render
from django.views import View


class AdminCarsView(View):
    def get(self, request):
        return render(request, 'adminka/cars/cars.html', {})
