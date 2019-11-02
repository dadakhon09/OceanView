from django.urls import path

from adminka.car.views import AdminCarsView
from adminka.news.views import AdminNewsView
from adminka.others.views import AdminIndexView, AdminLoginView, ProfileView, AdminLogoutView, ProfileUpdateView
from adminka.sights.views import AdminSightsView
from adminka.tours.views import AdminToursView, ToursCreateView, ToursUpdateView, ToursDeleteView
from adminka.villas.views import AdminVillasView

urlpatterns = [
    path('', AdminIndexView.as_view(), name='adminka-index'),

    path('cars/', AdminCarsView.as_view(), name='adminka-cars'),

    path('news/', AdminNewsView.as_view(), name='adminka-news'),

    path('sights/', AdminSightsView.as_view(), name='adminka-sights'),

    path('tours/', AdminToursView.as_view(), name='adminka-tours'),
    path('tours/create/', ToursCreateView.as_view(), name='tours-create'),
    path('tours/update/<int:id>/', ToursUpdateView.as_view(), name='tours-update'),
    path('tours/delete/<int:id>/', ToursDeleteView.as_view(), name='tours-delete'),

    path('villas/', AdminVillasView.as_view(), name='adminka-villas'),

    path('login/', AdminLoginView.as_view(), name='adminka-login'),
    path('profile/', ProfileView.as_view(), name='adminka-profile'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('logout/', AdminLogoutView.as_view(), name='adminka-logout'),
]
