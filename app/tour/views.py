from django.shortcuts import render
from django.views import View


class ToursView(View):
    def get(self, request):
        return render(request, 'tours.html', {})

