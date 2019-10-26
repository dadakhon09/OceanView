from django.shortcuts import render
from django.views import View


def handler404(request, exception):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html', {})


class AboutView(View):
    def get(self, request):
        return render(request, 'about.html', {})
