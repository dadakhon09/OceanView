from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse

from app.models import News


class AdminNewsView(View):
    def get(self, request):
        news_list = News.objects.all()
        return render(request, 'adminka/news/news.html', {'news_list': news_list})


class NewsCreateView(View):
	def get(self, request):
		return render(request, 'adminka/news/news_create.html')

	def post(self, request):
		post = self.request.POST

		title_en = post.get('title_en')
		title_ar = post.get('title_ar')
		title_fa = post.get('title_fa')
		title_hi = post.get('title_hi')
		title_ru = post.get('title_ru')
		title_zh = post.get('title_zh')

		title = {
            'title_en': title_en,
            'title_ar': title_ar,
            'title_fa': title_fa,
            'title_hi': title_hi,
            'title_ru': title_ru,
            'title_zh': title_zh,
        }
		
		description_en = post.get('description_en')
		description_ar = post.get('description_ar')
		description_fa = post.get('description_fa')
		description_hi = post.get('description_hi')
		description_ru = post.get('description_ru')
		description_zh = post.get('description_zh')
        
		description = {
            'description_en': description_en,
            'description_ar': description_ar,
            'description_fa': description_fa,
            'description_hi': description_hi,
            'description_ru': description_ru,
            'description_zh': description_zh,
        }


		image = post.get('image')

		news = News.objects.create(title=title, description=description, image=image)

		return HttpResponseRedirect(reverse('adminka-news'))



class NewsUpdateView(View):
	def get(self, request, id):
		news = News.objects.get(id=id)
		return render(request, 'adminka/news/news_update.html', {'news': news})

	def post(self, request, id):
		news = News.objects.get(id=id)

		post = self.request.POST

		title_en = post.get('title_en')
		title_ar = post.get('title_ar')
		title_fa = post.get('title_fa')
		title_hi = post.get('title_hi')
		title_ru = post.get('title_ru')
		title_zh = post.get('title_zh')

		title = {
            'title_en': title_en,
            'title_ar': title_ar,
            'title_fa': title_fa,
            'title_hi': title_hi,
            'title_ru': title_ru,
            'title_zh': title_zh,
        }
		
		description_en = post.get('description_en')
		description_ar = post.get('description_ar')
		description_fa = post.get('description_fa')
		description_hi = post.get('description_hi')
		description_ru = post.get('description_ru')
		description_zh = post.get('description_zh')
        
		description = {
            'description_en': description_en,
            'description_ar': description_ar,
            'description_fa': description_fa,
            'description_hi': description_hi,
            'description_ru': description_ru,
            'description_zh': description_zh,
        }


		image = post.get('image')

		news.title = title
		news.description = description
		news.image = image
		news.save()

		return HttpResponseRedirect(reverse('adminka-news'))


class NewsDeleteView(View):
	def get(self, request, id):
		news = News.objects.get(id=id)
		news.delete()
		return HttpResponseRedirect(reverse('adminka-news'))
		