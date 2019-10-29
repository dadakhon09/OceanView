"""OceanView URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.utils import translation
from django.shortcuts import redirect
from app.others.views import handler404 as h404
from app.others.views import handler500 as h500

handler404 = h404
handler500 = h500


def set_language(request):
    language = request.POST.get('language', settings.LANGUAGE_CODE)
    translation.activate(language)
    request.session[translation.LANGUAGE_SESSION_KEY] = language
    return redirect('adminka-index')


urlpatterns = [
    # path('', include('app.urls')),
    path('admin/', admin.site.urls),
    path('set_lang/<str:language>/', set_language, name='set_language'),
]

urlpatterns += i18n_patterns(
    path('', include('app.urls')),
    path('admin/', include('adminka.urls')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
