from django.urls import path

from adminka.car.views import AdminCarsView
from adminka.news.views import AdminNewsView
from adminka.others.views import AdminIndexView
from adminka.sights.views import AdminSightsView
from adminka.tours.views import AdminToursView
from adminka.villas.views import AdminVillasView

urlpatterns = [
    path('', AdminIndexView.as_view(), name='adminka-index'),
    path('cars/', AdminCarsView.as_view(), name='adminka-cars'),
    path('news/', AdminNewsView.as_view(), name='adminka-news'),
    path('sights/', AdminSightsView.as_view(), name='adminka-sights'),
    path('tours/', AdminToursView.as_view(), name='adminka-tours'),
    path('villas/', AdminVillasView.as_view(), name='adminka-villas'),
]
