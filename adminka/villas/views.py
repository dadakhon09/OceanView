from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse

from app.models import Villa


class AdminVillasView(View):
    def get(self, request):
        villas = Villa.objects.all()

        return render(request, 'adminka/villas/villas.html', {'villas': villas})


class VillasCreateView(View):
	def get(self, request):
		return render(request, 'adminka/villas/villas_create.html')


class VillasUpdateView(View):
	def get(self, request, id):
		return render(request, 'adminka/villas/villas_update.html')


class VillasDeleteView(View):
	def get(self, request, id):
		v = Villa.objects.get(id=id)
		v.delete()
		return HttpResponseRedirect(reverse('adminka-villas'))

