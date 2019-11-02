from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from app.models import Tour


class AdminToursView(View):
    def get(self, request):
        tours = Tour.objects.all()

        return render(request, 'adminka/tours.html', {'tours': tours})


class ToursCreateView(View):
    def get(self, request):
        return render(request, 'adminka/tours_create.html', {})

    def post(self, request):

        post = self.request.POST

        title_en = post.get('title_en')
        title_ar = post.get('title_ar')
        title_fa = post.get('title_fa')
        title_hi = post.get('title_hi')
        title_ru = post.get('title_ru')
        title_zh = post.get('title_zh')

        plan_en = post.get('plan_en')
        plan_ar = post.get('plan_ar')
        plan_fa = post.get('plan_fa')
        plan_hi = post.get('plan_hi')
        plan_ru = post.get('plan_ru')
        plan_zh = post.get('plan_zh')

        description_en = post.get('description_en')
        description_ar = post.get('description_ar')
        description_fa = post.get('description_fa')
        description_hi = post.get('description_hi')
        description_ru = post.get('description_ru')
        description_zh = post.get('description_zh')

        route_en = post.get('route_en')
        route_ar = post.get('route_ar')
        route_fa = post.get('route_fa')
        route_hi = post.get('route_hi')
        route_ru = post.get('route_ru')
        route_zh = post.get('route_zh')

        duration = post.get('duration')

        image = post.get('image')

        num_people = post.get('num_people')

        guide = post.get('guide')

        price = post.get('price')

        title = {
            'title_en': title_en,
            'title_ar': title_ar,
            'title_fa': title_fa,
            'title_hi': title_hi,
            'title_ru': title_ru,
            'title_zh': title_zh,
        }

        description = {
            'description_en': description_en,
            'description_ar': description_ar,
            'description_fa': description_fa,
            'description_hi': description_hi,
            'description_ru': description_ru,
            'description_zh': description_zh,
        }

        plan = {
            'plan_en': plan_en,
            'plan_ar': plan_ar,
            'plan_fa': plan_fa,
            'plan_hi': plan_hi,
            'plan_ru': plan_ru,
            'plan_zh': plan_zh,
        }

        route = {
            'route_en': route_en,
            'route_ar': route_ar,
            'route_fa': route_fa,
            'route_hi': route_hi,
            'route_ru': route_ru,
            'route_zh': route_zh,
        }

        tour = Tour.objects.create(title=title, description=description, plan=plan, route=route, image=image,
                                   duration=duration, num_people=num_people, guide=guide, price=price)

        return HttpResponseRedirect(reverse('adminka-tours'))


class ToursUpdateView(View):
    pass