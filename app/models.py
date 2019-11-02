import jsonfield
from django.db import models
# from django.db.backends.postgresql import

from phone_field import PhoneField


class About(models.Model):
    text = models.TextField()

    class Meta:
        db_table = 'about'

    def __str__(self):
        return self.text[:100]


class AboutImage(models.Model):
    image = models.ImageField(upload_to='about')
    about = models.ForeignKey(About, on_delete=models.CASCADE)

    class Meta:
        db_table = 'about-images'


class SightCategory(models.Model):
    # name = models.CharField(max_length=255, null=True, blank=True)
    name = jsonfield.JSONField()

    class Meta:
        db_table = 'categories'

    def __str__(self):
        for key in self.name.values():
            first = key
            return first


class Facility(models.Model):
    # name = models.CharField(max_length=255)
    name = jsonfield.JSONField()
    image = models.ImageField(upload_to='facilities', null=True, blank=True)
    tour = models.ManyToManyField('Tour', related_name='tour_facilities')

    class Meta:
        db_table = 'facilities'

    def __str__(self):
        for key in self.name.values():
            first = key
            return first


class Expense(models.Model):
    # name = models.CharField(max_length=255)
    name = jsonfield.JSONField()
    image = models.ImageField(upload_to='expenses', null=True, blank=True)
    tour = models.ManyToManyField('Tour', related_name='tour_expenses')

    class Meta:
        db_table = 'expenses'

    def __str__(self):
        for key in self.name.values():
            first = key
            return first


class VillaImage(models.Model):
    image = models.ImageField(upload_to='villas', null=True, blank=True)
    villa = models.ForeignKey('Villa', on_delete=models.CASCADE)

    class Meta:
        db_table = 'villa_images'


class VillaPhoneNumber(models.Model):
    phone = PhoneField(null=True, blank=True, help_text='Contact phone number')
    villa = models.ForeignKey('Villa', on_delete=models.CASCADE)

    class Meta:
        db_table = 'villa_phone_numbers'

    def __str__(self):
        return str(self.phone)


class Tour(models.Model):
    # title = models.CharField(max_length=255)
    title = jsonfield.JSONField()
    # description = models.TextField(null=True, blank=True)
    description = jsonfield.JSONField()
    image = models.ImageField(upload_to='tours', null=True, blank=True)
    route = jsonfield.JSONField()                                          # ASK
    duration = models.PositiveIntegerField(null=True, blank=True)
    num_people = models.PositiveIntegerField(blank=True, null=True)
    guide = models.BooleanField(null=True, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)
    # plan = models.TextField(null=True, blank=True)
    plan = jsonfield.JSONField()

    class Meta:
        db_table = 'tours'

    def __str__(self):
        for key in self.title.values():
            first = key
            return first


class Sight(models.Model):
    # title = models.CharField(max_length=255)
    title = jsonfield.JSONField()
    # description = models.TextField(null=True, blank=True)
    description = jsonfield.JSONField()
    image = models.ImageField(upload_to='sights', null=True, blank=True)
    category = models.ForeignKey(SightCategory, on_delete=models.CASCADE)

    class Meta:
        db_table = 'sights'

    def __str__(self):
        for key in self.title.values():
            first = key
            return first


class VillaServiceCategory(models.Model):
    # name = models.CharField(max_length=255)
    name = jsonfield.JSONField()

    class Meta:
        db_table = 'villa_service_categories'

    def __str__(self):
        for key in self.name.values():
            first = key
            return first


class VillaService(models.Model):
    # name = models.CharField(max_length=255)
    name = jsonfield.JSONField()
    category = models.ForeignKey(VillaServiceCategory, on_delete=models.CASCADE)
    villa = models.ManyToManyField('Villa', related_name='villas')

    class Meta:
        db_table = 'villa_services'

    def __str__(self):
        for key in self.name.values():
            first = key
            return first


class Villa(models.Model):
    # title = models.CharField(max_length=255)
    title = jsonfield.JSONField()
    address = models.CharField(max_length=255, null=True, blank=True)
    # description = models.TextField(null=True, blank=True)
    description = jsonfield.JSONField()
    bedroom = models.PositiveIntegerField(null=True, blank=True)
    square_meter = models.PositiveIntegerField(null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    d_center = models.PositiveIntegerField(null=True, blank=True)
    d_airways = models.PositiveIntegerField(null=True, blank=True)
    d_railways = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        db_table = 'villas'

    def __str__(self):
        for key in self.title.values():
            first = key
            return first


class News(models.Model):
    title = jsonfield.JSONField()
    # title = models.CharField(max_length=255, blank=True, null=True)
    # description = models.TextField(null=True, blank=True)
    description = jsonfield.JSONField()
    image = models.ImageField(upload_to='news', blank=True, null=True)
    created = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'news'

    def __str__(self):
        for key in self.title.values():
            first = key
            return first
