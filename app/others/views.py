from django.shortcuts import render
from django.views import View

from app.models import Villa, Tour, Sight, News, Car, About


def handler404(request, exception):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)


class IndexView(View):
    def get(self, request):
        villas = Villa.objects.all()[:6][::-1]
        tours = Tour.objects.all()[:4][::-1]
        sights = Sight.objects.all()[:10][::-1]
        cars = Car.objects.all()[:10][::-1]
        news_list = News.objects.all()[:4][::-1]

        context = {
            'villas': villas,
            'tours': tours,
            'sights': sights,
            'cars': cars,
            'news_list': news_list,
        }
        return render(request, 'main/index.html', context)


class AboutView(View):
    def get(self, request):
        about = About.objects.get(id=1)
        return render(request, 'main/about.html', {'about': about})
