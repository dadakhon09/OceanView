from django.shortcuts import render
from django.views import View

from app.models import News


class AdminNewsView(View):
    def get(self, request):
        news = News.objects.all()

        return render(request, 'adminka/news/news.html', {'news': news})
