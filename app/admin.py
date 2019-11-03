from django.contrib import admin

from app.models import SightCategory, TourFacility, TourExpense, VillaPhoneNumber, Tour, Sight, Villa, News, \
    VillaServiceCategory, VillaService, About

admin.site.register(SightCategory)
admin.site.register(TourFacility)
admin.site.register(TourExpense)
admin.site.register(VillaPhoneNumber)
admin.site.register(Tour)
admin.site.register(VillaServiceCategory)
admin.site.register(VillaService)
admin.site.register(Sight)
admin.site.register(Villa)
admin.site.register(News)
admin.site.register(About)
