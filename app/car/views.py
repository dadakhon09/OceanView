from django.shortcuts import render
from django.views import View


class CarsView(View):
    def get(self, request):
        return render(request, 'main/cars.html', {})


class CarView(View):
	def get(self, request, id):
		return render(request, 'main/car_view.html', {})