from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View

from app.models import About, AboutImage


class AdminAboutView(View):
    def get(self, request):
        about = About.objects.get(id=1)
        a_images = AboutImage.objects.filter(about=about)
        return render(request, 'adminka/about/about.html', {'about': about, 'a_images': a_images})

    def post(self, request):
        about = About.objects.get(id=1)

        post = self.request.POST

        text_en = post.get('text_en')
        text_ar = post.get('text_ar')
        text_fa = post.get('text_fa')
        text_hi = post.get('text_hi')
        text_ru = post.get('text_ru')
        text_zh = post.get('text_zh')

        text = {
            'text_en': text_en,
            'text_ar': text_ar,
            'text_fa': text_fa,
            'text_hi': text_hi,
            'text_ru': text_ru,
            'text_zh': text_zh,
        }

        about.text = text
        about.save()

        images = self.request.FILES.getlist('image')

        for i in images:
            ai, _ = AboutImage.objects.get_or_create(image=i, about=about)

        return HttpResponseRedirect(reverse('adminka-index'))
