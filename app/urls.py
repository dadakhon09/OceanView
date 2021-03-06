from django.urls import path

from app.sights.views import SightsView, SightView
from app.car.views import CarsView, CarView
from app.news.views import NewsView, NewsSingleView
from app.others.views import AboutView, IndexView
from app.tours.views import ToursView, TourView
from app.villas.views import VillasView, VillaView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('tours/', ToursView.as_view(), name='tours'),
    path('tours/<str:slug>/', TourView.as_view(), name='tour-view'),
    path('villas/', VillasView.as_view(), name='villas'),
    path('villas/<str:slug>/', VillaView.as_view(), name='villa-view'),
    path('cars/', CarsView.as_view(), name='cars'),
    path('cars/<str:slug>/', CarView.as_view(), name='car-view'),
    path('news/', NewsView.as_view(), name='news'),
    path('news/<str:slug>/', NewsSingleView.as_view(), name='news-view'),
    path('sights/', SightsView.as_view(), name='sights'),
    path('sights/<str:slug>/', SightView.as_view(), name='sight-view'),
]
