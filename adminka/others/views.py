from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from app.models import Villa, Tour, Sight, News


class AdminIndexView(View):
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
        return render(request, 'adminka/index.html', context)


class AdminLoginView(View):
    def get(self, request):
        return render(request, 'adminka/login.html', {})


class AdminLogoutView(LoginRequiredMixin, View):
    pass


class ProfileView(View):
    def get(self, request):
        user = self.request.user
        return render(request, 'adminka/profile.html', {'user': user})

