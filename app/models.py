import jsonfield
from django.core.files.storage import FileSystemStorage
from django.db import models
# from django.db.backends.postgresql import

from phone_field import PhoneField


class About(models.Model):
    text = jsonfield.JSONField()

    class Meta:
        db_table = 'about'
        ordering = ['-id']

    def __str__(self):
        return self.text['text_en'][:100]


class AboutImage(models.Model):
    image = models.ImageField(upload_to='about', null=True, blank=True)
    about = models.ForeignKey(About, on_delete=models.CASCADE)

    class Meta:
        db_table = 'about-images'
        ordering = ['-id']

    def __str__(self):
        return self.image.name


class TourFacility(models.Model):
    # title = models.CharField(max_length=255)
    title = jsonfield.JSONField()
    image = models.ImageField(upload_to='facilities', null=True, blank=True)
    tours = models.ManyToManyField('Tour', related_name='t_facilities')

    class Meta:
        db_table = 'facilities'
        ordering = ['-id']

    def __str__(self):
        return self.title['title_en']


class TourExpense(models.Model):
    # title = models.CharField(max_length=255)
    title = jsonfield.JSONField()
    image = models.ImageField(upload_to='expenses', null=True, blank=True)
    tours = models.ManyToManyField('Tour', related_name='t_expenses')

    class Meta:
        db_table = 'expenses'
        ordering = ['-id']

    def __str__(self):
        return self.title['title_en']


class TourImage(models.Model):
    image = models.ImageField(upload_to='tours', null=True, blank=True)
    tour = models.ForeignKey('Tour', on_delete=models.CASCADE, related_name='images')

    class Meta:
        db_table = 'tour_images'
        ordering = ['-id']

    def __str__(self):
        return self.image.name


class Tour(models.Model):
    # title = models.CharField(max_length=255)
    title = jsonfield.JSONField()
    # description = models.TextField(null=True, blank=True)
    description = jsonfield.JSONField()
    route = jsonfield.JSONField()  # ASK
    duration = models.PositiveIntegerField(null=True, blank=True)
    num_people = models.PositiveIntegerField(blank=True, null=True)
    guide = models.BooleanField(null=True, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)
    # plan = models.TextField(null=True, blank=True)
    plan = jsonfield.JSONField()

    class Meta:
        db_table = 'tours'
        ordering = ['-id']

    def __str__(self):
        return self.title['title_en']


class SightCategory(models.Model):
    # title = models.CharField(max_length=255, null=True, blank=True)
    title = jsonfield.JSONField()

    class Meta:
        db_table = 'sight_categories'
        ordering = ['-id']

    def __str__(self):
        return self.title['title_en']


class SightImage(models.Model):
    image = models.ImageField(upload_to='sights', null=True, blank=True)
    sight = models.ForeignKey('Sight', on_delete=models.CASCADE, related_name='s_images')

    class Meta:
        db_table = 'sight_images'
        ordering = ['-id']

    def __str__(self):
        return self.image.name


class Sight(models.Model):
    # title = models.CharField(max_length=255)
    title = jsonfield.JSONField()
    # description = models.TextField(null=True, blank=True)
    description = jsonfield.JSONField()
    category = models.ForeignKey(SightCategory, on_delete=models.CASCADE)

    class Meta:
        db_table = 'sights'
        ordering = ['-id']

    def __str__(self):
        return self.title['title_en']


class VillaImage(models.Model):
    image = models.ImageField(upload_to='villas', null=True, blank=True)
    villa = models.ForeignKey('Villa', on_delete=models.CASCADE)

    class Meta:
        db_table = 'villa_images'
        ordering = ['-id']

    def __str__(self):
        return self.image.name


# class VillaPhoneNumber(models.Model):
#     phone = PhoneField(null=True, blank=True, help_text='Contact phone number')
#     villa = models.ForeignKey('Villa', on_delete=models.CASCADE)

#     class Meta:
#         db_table = 'villa_phone_numbers'

#     def __str__(self):
#         return str(self.phone)


class VillaServiceCategory(models.Model):
    # title = models.CharField(max_length=255)
    title = jsonfield.JSONField()

    class Meta:
        db_table = 'villa_service_categories'
        ordering = ['-id']

    def __str__(self):
        return self.title['title_en']


class VillaService(models.Model):
    # title = models.CharField(max_length=255)
    title = jsonfield.JSONField()
    category = models.ForeignKey(VillaServiceCategory, on_delete=models.CASCADE)
    villas = models.ManyToManyField('Villa', related_name='v_services')

    class Meta:
        db_table = 'villa_services'
        ordering = ['-id']

    def __str__(self):
        return self.title['title_en']


STATUS = (
    ('Signature villa', 0),
    ('Garden home villa', 1),
)


class Villa(models.Model):
    # title = models.CharField(max_length=255)
    title = jsonfield.JSONField()
    address = jsonfield.JSONField()
    # description = models.TextField(null=True, blank=True)
    description = jsonfield.JSONField()
    phone = models.CharField(max_length=255, null=True, blank=True)
    bedroom = models.PositiveIntegerField(null=True, blank=True)
    square_meter = models.PositiveIntegerField(null=True, blank=True)
    status = models.IntegerField(choices=STATUS, null=True, blank=True)
    d_center = models.PositiveIntegerField(null=True, blank=True)
    d_airways = models.PositiveIntegerField(null=True, blank=True)
    d_railways = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        db_table = 'villas'
        ordering = ['-id']

    def __str__(self):
        return self.title['title_en']


class News(models.Model):
    title = jsonfield.JSONField()
    # title = models.CharField(max_length=255, blank=True, null=True)
    # description = models.TextField(null=True, blank=True)
    description = jsonfield.JSONField()
    image = models.ImageField(upload_to='news', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'news'
        ordering = ['-id']

    def __str__(self):
        return self.title['title_en']


class CarImage(models.Model):
    image = models.ImageField(upload_to='cars', null=True, blank=True)
    car = models.ForeignKey('Car', on_delete=models.CASCADE)

    class Meta:
        db_table = 'car_images'
        ordering = ['-id']

    def __str__(self):
        return self.image.name


class Car(models.Model):
    title = jsonfield.JSONField()
    description = jsonfield.JSONField()
    price = models.PositiveIntegerField(null=True, blank=True)
    duration = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        db_table = 'cars'
        ordering = ['-id']

    def __str__(self):
        return self.title['title_en']
