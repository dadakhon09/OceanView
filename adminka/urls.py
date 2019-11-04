from django.urls import path

from adminka.car.views import AdminCarsView
from adminka.news.views import AdminNewsView, NewsCreateView, NewsUpdateView, NewsDeleteView
from adminka.others.views import AdminIndexView, AdminLoginView, ProfileView, AdminLogoutView, ProfileUpdateView
from adminka.sights.views import AdminSightsView, SightsCreateView, SightsUpdateView, SightsDeleteView, SightsCategoriesView, SightsCategoriesCreateView, SightsCategoriesUpdateView, SightsCategoriesDeleteView
from adminka.tours.views import AdminToursView, ToursCreateView, ToursUpdateView, ToursDeleteView, \
    AdminToursExpensesView, AdminToursFacilitiesView, AdminToursExpensesUpdateView, AdminToursExpensesDeleteView, \
    AdminToursFacilitiesUpdateView, AdminToursFacilitiesDeleteView, AdminToursExpensesCreateView, \
    AdminToursFacilitiesCreateView
from adminka.villas.views import AdminVillasView

urlpatterns = [
    path('', AdminIndexView.as_view(), name='adminka-index'),

    path('cars/', AdminCarsView.as_view(), name='adminka-cars'),

    path('news/', AdminNewsView.as_view(), name='adminka-news'),
    path('news/create/', NewsCreateView.as_view(), name='news-create'),
    path('news/update/<int:id>/', NewsUpdateView.as_view(), name='news-update'),
    path('news/delete/<int:id>/', NewsDeleteView.as_view(), name='news-delete'),

    path('sights/', AdminSightsView.as_view(), name='adminka-sights'),
    path('sights/create/', SightsCreateView.as_view(), name='sights-create'),
    path('sights/update/<int:id>/', SightsUpdateView.as_view(), name='sights-update'),
    path('sights/delete/<int:id>/', SightsDeleteView.as_view(), name='sights-delete'),
    path('sights/categories/', SightsCategoriesView.as_view(), name='sight-categories'),
    path('sights/categories/create/', SightsCategoriesCreateView.as_view(), name='sight-categories-create'),
    path('sights/categories/update/<int:id>/', SightsCategoriesUpdateView.as_view(), name='sight-categories-update'),
    path('sights/categories/delete/<int:id>/', SightsCategoriesDeleteView.as_view(), name='sight-categories-delete'),

    path('tours/', AdminToursView.as_view(), name='adminka-tours'),
    path('tours/create/', ToursCreateView.as_view(), name='tours-create'),
    path('tours/update/<int:id>/', ToursUpdateView.as_view(), name='tours-update'),
    path('tours/delete/<int:id>/', ToursDeleteView.as_view(), name='tours-delete'),
    path('tours/expenses/', AdminToursExpensesView.as_view(), name='tour-expenses'),
    path('tours/expenses/create/', AdminToursExpensesCreateView.as_view(), name='tour-expenses-create'),
    path('tours/expenses/update/<int:id>/', AdminToursExpensesUpdateView.as_view(), name='tour-expenses-update'),
    path('tours/expenses/delete/<int:id>/', AdminToursExpensesDeleteView.as_view(), name='tour-expenses-delete'),
    path('tours/facilities/', AdminToursFacilitiesView.as_view(), name='tour-facilities'),
    path('tours/facilities/create/', AdminToursFacilitiesCreateView.as_view(), name='tour-facilities-create'),
    path('tours/facilities/update/<int:id>/', AdminToursFacilitiesUpdateView.as_view(), name='tour-facilities-update'),
    path('tours/facilities/delete/<int:id>/', AdminToursFacilitiesDeleteView.as_view(), name='tour-facilities-delete'),

    path('villas/', AdminVillasView.as_view(), name='adminka-villas'),
    # path('villas/create/', VillasCreateView.as_view(), name='villas-create'),
    # path('villas/update/<int:id>/', VillasUpdateView.as_view(), name='villas-update'),
    # path('villas/delete/<int:id>/', VillasDeleteView.as_view(), name='villas-delete'),

    path('login/', AdminLoginView.as_view(), name='adminka-login'),
    path('profile/', ProfileView.as_view(), name='adminka-profile'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('logout/', AdminLogoutView.as_view(), name='adminka-logout'),
]
