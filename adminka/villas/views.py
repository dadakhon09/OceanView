from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse

from app.models import Villa, VillaService, VillaServiceCategory


class AdminVillasView(View):
    def get(self, request):
        villas = Villa.objects.all()
        return render(request, 'adminka/villas/villas.html', {'villas': villas})


class VillasCreateView(View):
	def get(self, request):
		return render(request, 'adminka/villas/villas_create.html')


class VillasUpdateView(View):
	def get(self, request, id):
		villa = Villa.objects.get(id=id)
		return render(request, 'adminka/villas/villas_update.html', {'villa': villa})


class VillasDeleteView(View):
	def get(self, request, id):
		v = Villa.objects.get(id=id)
		v.delete()
		return HttpResponseRedirect(reverse('adminka-villas'))


class VillaServicesView(View):
    def get(self, request):
        v_services = VillaService.objects.all()

        return render(request, 'adminka/villas/villa_services.html', {'v_services': v_services})


class VillaServicesCreateView(View):
	def get(self, request):
		return render(request, 'adminka/villas/villa_services_create.html')


class VillaServicesUpdateView(View):
	def get(self, request, id):
		v_service = VillaService.objects.get(id=id)
		return render(request, 'adminka/villas/villa_services_update.html', {'v_service', v_service})


class VillaServicesDeleteView(View):
	def get(self, request, id):
		v = VillaService.objects.get(id=id)
		v.delete()
		return HttpResponseRedirect(reverse('villa-services'))


class VillaServiceCategoriesView(View):
    def get(self, request):
        v_service_categories = VillaServiceCategory.objects.all()

        return render(request, 'adminka/villas/villa_service_categories.html', {'v_service_categories': v_service_categories})


class VillaServiceCategoriesCreateView(View):
	def get(self, request):
		return render(request, 'adminka/villas/villa_service_categories_create.html')


class VillaServiceCategoriesUpdateView(View):
	def get(self, request, id):
		v_service_category = VillaServiceCategory.objects.get(id=id)
		return render(request, 'adminka/villas/villa_service_categories_update.html', {'v_service_category': v_service_category})


class VillaServiceCategoriesDeleteView(View):
	def get(self, request, id):
		v = VillaServiceCategory.objects.get(id=id)
		v.delete()
		return HttpResponseRedirect(reverse('villa-service-categories'))
