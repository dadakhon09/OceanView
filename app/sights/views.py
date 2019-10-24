from django.shortcuts import render
from django.views import View


class SightsView(View):
    def get(self, request):
        return render(request, 'sights.html', {})
