from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import UpdateView

from app.models import Tour, TourExpense, TourFacility


class AdminToursView(View):
    def get(self, request):
        tours = Tour.objects.all()

        return render(request, 'adminka/tours/tours.html', {'tours': tours})


class ToursCreateView(View):
    def get(self, request):
        return render(request, 'adminka/tours/tours_create.html', {})

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
        if not duration:
            duration = None

        num_people = post.get('num_people')

        if not num_people:
            num_people = None

        guide = post.get('guide')

        price = post.get('price')

        if not price:
            price = None

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

        tour = Tour.objects.create(title=title, description=description, plan=plan, route=route,
                                   duration=duration, num_people=num_people, guide=guide, price=price)

        return HttpResponseRedirect(reverse('adminka-tours'))


class ToursUpdateView(View):
    # model = Tour
    # template_name = 'adminka/tours_update.html'
    # fields = ['title', 'plan', 'description', 'route', 'image', 'duration', 'num_people', 'guide', 'price']

    def get(self, request, id):
        tour = Tour.objects.get(id=self.kwargs['id'])
        return render(request, 'adminka/tours/tours_update.html', {'tour': tour})

    def post(self, request, id):
        tour = Tour.objects.get(id=self.kwargs['id'])

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
        if not duration:
            duration = None

        num_people = post.get('num_people')

        if not num_people:
            num_people = None

        guide = post.get('guide')

        price = post.get('price')

        if not price:
            price = None

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

        tour.title = title
        tour.description = description
        tour.plan = plan
        tour.route = route
        tour.duration = duration
        tour.num_people = num_people
        tour.guide = guide
        tour.price = price

        tour.save()

        return HttpResponseRedirect(reverse('adminka-tours'))


class ToursDeleteView(View):
    def get(self, request, id):
        tour = Tour.objects.get(id=id)
        tour.delete()
        return HttpResponseRedirect(reverse('adminka-tours'))


class AdminToursExpensesView(View):
    def get(self, request):
        tour_expenses = TourExpense.objects.all()
        return render(request, 'adminka/tours/tour_expenses.html', {'tours': tour_expenses})


class AdminToursExpensesCreateView(View):
    def get(self, request):
        return render(request, 'adminka/tours/tour_expenses_create.html')

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

        image = post.get('image')

        TourExpense.objects.create(title=title, image=image)

        return HttpResponseRedirect(reverse('tour-expenses'))


class AdminToursExpensesUpdateView(View):
    def get(self, request, id):
        t_expense = TourExpense.objects.get(id=id)
        return render(request, 'adminka/tours/tour_expenses.html', {'tour': t_expense})


class AdminToursExpensesDeleteView(View):
    def get(self, request, id):
        t = TourExpense.objects.get(id=id)
        t.delete()
        return HttpResponseRedirect(reverse('tour-expenses'))


class AdminToursFacilitiesView(View):
    def get(self, request):
        tour_facilities = TourFacility.objects.all()
        return render(request, 'adminka/tours/tour_facilities.html', {'tours': tour_facilities})


class AdminToursFacilitiesCreateView(View):
    def get(self, request):
        return render(request, 'adminka/tours/tour_facilities_create.html')


class AdminToursFacilitiesUpdateView(View):
    def get(self, request, id):
        t_facility = TourFacility.objects.get(id=id)
        return render(request, 'adminka/tours/tour_expenses.html', {'tour': t_facility})


class AdminToursFacilitiesDeleteView(View):
    def get(self, request, id):
        t = TourFacility.objects.get(id=id)
        t.delete()
        return HttpResponseRedirect(reverse('tour-facilities'))
