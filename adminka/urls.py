from django.urls import path

from adminka.others.views import AdminIndexView

urlpatterns = [
    path('', AdminIndexView.as_view(), name='adminka-index'),
]
