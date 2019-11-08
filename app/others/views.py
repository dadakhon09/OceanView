from django.shortcuts import render
from django.views import View

from app.models import Villa, Tour, Sight, News


def handler404(request, exception):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)


class IndexView(View):
    def get(self, request):
        villas = Villa.objects.all().order_by('-id')[:6][::-1]
        tours = Tour.objects.all().order_by('-id')[:4][::-1]
        sights = Sight.objects.all().order_by('-id')[:10][::-1]
        news = News.objects.all().order_by('-id')[:4][::-1]

        context = {
            'villas': villas,
            'tours': tours,
            'sights': sights,
            'news': news,
        }
        return render(request, 'main/index.html', context)


class AboutView(View):
    def get(self, request):
        return render(request, 'main/about.html', {})
