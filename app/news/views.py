from django.shortcuts import render
from django.views import View

from app.models import News


class NewsView(View):
    def get(self, request):
        news = News.objects.all()

        return render(request, 'main/news.html', {'news': news})


class NewsSingleView(View):
	def get(self, request, id):
		return render(request, 'main/news_view.html')