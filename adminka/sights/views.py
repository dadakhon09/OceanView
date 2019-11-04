from django.shortcuts import render
from django.views import View

from app.models import Sight, SightCategory


class AdminSightsView(View):
    def get(self, request):
        sights = Sight.objects.all()
        return render(request, 'adminka/sights/sights.html', {'sights': sights})


class SightsCreateView(View):
	def get(self, request):
		return render(request, 'adminka/sights/sights_create.html')


class SightsUpdateView(View):
	def get(self, request, id):
		sight = Sight.objects.get(id=id)
		return render(request, 'adminka/sights/sights_update.html', {'sight': sight})


class SightsDeleteView(View):
	def get(self, request, id):
		c = SightCategory.objects.get(id=id)
		c.delete()
		return HttpResponseRedirect(reverse('adminka-sights'))


class SightsCategoriesView(View):
	def get(self, request):
		s_categories = SightCategory.objects.all()
		return render(request, 'adminka/sights/sight_categories.html')


class SightsCategoriesCreateView(View):
	def get(self, request):
		return render(request, 'adminka/sights/sight_categories_create.html')

	def post(self, request):
		


class SightsCategoriesUpdateView(View):
	def get(self, request, id):
		s_category = SightCategory.objects.get(id=id)
		return render(request, 'adminka/sights/sight_categories_update.html', {'s_category': s_category})


class SightsCategoriesDeleteView(View):
	def get(self, request, id):
		c = SightCategory.objects.get(id=id)
		c.delete()
		return HttpResponseRedirect(reverse('sight-categories'))
