from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from app.models import Sight, SightCategory


class AdminSightsView(View):
    def get(self, request):
        sights = Sight.objects.all()

        page = request.GET.get('page', 1)

        paginator = Paginator(sights, 15)
        try:
            sights = paginator.page(page)
        except PageNotAnInteger:
            sights = paginator.page(1)
        except EmptyPage:
            sights = paginator.page(paginator.num_pages)

        return render(request, 'adminka/sights/sights.html', {'sights': sights})


class SightsCreateView(View):
	def get(self, request):
		s_categories = SightCategory.objects.all()
		return render(request, 'adminka/sights/sights_create.html', {'s_categories': s_categories})

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

		c = post.get('category')
		category = SightCategory.objects.get(id=int(c))

		images = post.getlist('images')



		sight = Sight.objects.create(title=title, description=description, category=category)

		if images:
			for i in images:
				si = SightImage.objects.create(image=i, sight=sight)
				sight.images.add(si)
				sight.save()

		return HttpResponseRedirect(reverse('adminka-sights'))


class SightsUpdateView(View):
	def get(self, request, id):
		sight = Sight.objects.get(id=id)
		s_categories = SightCategory.objects.exclude(id=sight.category.id)
		return render(request, 'adminka/sights/sights_update.html', {'sight': sight, 's_categories': s_categories})

	def post(self, request, id):
		sight = Sight.objects.get(id=id)
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

		c = post.get('category')
		category = SightCategory.objects.get(id=int(c))

		images = post.getlist('images')

		sight.title = title
		sight.description = description
		sight.category = category
		sight.save()

		if images:
			for i in images:
				si = SightImage.objects.create(image=i, sight=sight)
				sight.images.add(si)
				sight.save()

		return HttpResponseRedirect(reverse('adminka-sights'))



class SightsDeleteView(View):
	def get(self, request, id):
		c = SightCategory.objects.get(id=id)
		c.delete()
		return HttpResponseRedirect(reverse('adminka-sights'))


class SightsCategoriesView(View):
	def get(self, request):
		s_categories = SightCategory.objects.all()
		return render(request, 'adminka/sights/sight_categories.html', {'s_categories': s_categories})


class SightsCategoriesCreateView(View):
	def get(self, request):
		return render(request, 'adminka/sights/sight_categories_create.html')

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

		SightCategory.objects.create(title=title)
		
		return HttpResponseRedirect(reverse('sight-categories'))


class SightsCategoriesUpdateView(View):
	def get(self, request, id):
		s_category = SightCategory.objects.get(id=id)
		return render(request, 'adminka/sights/sight_categories_update.html', {'s_category': s_category})

	def post(self, request, id):
		s_category = SightCategory.objects.get(id=id)

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
		
		s_category.title = title
		s_category.save()
		
		return HttpResponseRedirect(reverse('sight-categories'))


class SightsCategoriesDeleteView(View):
	def get(self, request, id):
		c = SightCategory.objects.get(id=id)
		c.delete()
		return HttpResponseRedirect(reverse('sight-categories'))
