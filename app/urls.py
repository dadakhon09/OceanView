from django.urls import path

from app.sights.views import SightsView
from app.car.views import CarsView
from app.news.views import NewsView
from app.others.views import AboutView, IndexView
from app.tours.views import ToursView
from app.villas.views import VillasView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('tours/', ToursView.as_view(), name='tours'),
    path('villas/', VillasView.as_view(), name='villas'),
    path('cars/', CarsView.as_view(), name='cars'),
    path('news/', NewsView.as_view(), name='news'),
    path('sights/', SightsView.as_view(), name='sights'),
]
