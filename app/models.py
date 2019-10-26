from django.db import models

from phone_field import PhoneField


class SightCategory(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.name


class Facility(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='facilities', null=True, blank=True)
    tour = models.ManyToManyField('Tour', related_name='tours')

    class Meta:
        db_table = 'facilities'

    def __str__(self):
        return self.name


class Expense(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='expenses', null=True, blank=True)
    tour = models.ManyToManyField('Tour', related_name='tours')

    class Meta:
        db_table = 'expenses'

    def __str__(self):
        return self.name


class VillaImage(models.Model):
    image = models.ImageField(upload_to='villas', null=True, blank=True)
    villa = models.ForeignKey('Villa', on_delete=models.CASCADE)


class VillaPhoneNumber(models.Model):
    phone = PhoneField(null=True, blank=True, help_text='Contact phone number')
    villa = models.ForeignKey('Villa', on_delete=models.CASCADE)

    class Meta:
        db_table = 'villa_phone_numbers'

    def __str__(self):
        return self.phone


class Tour(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='tours', null=True, blank=True)
    route = models.CharField(max_length=255, null=True, blank=True)
    duration = models.PositiveIntegerField(null=True, blank=True)
    max_people = models.PositiveIntegerField(null=True, blank=True)
    guide = models.BooleanField(null=True, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)
    plan = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'tours'

    def __str__(self):
        return self.title


class Sight(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='sights', null=True, blank=True)
    category = models.ForeignKey(SightCategory, on_delete=models.CASCADE)

    class Meta:
        db_table = 'sights'

    def __str__(self):
        return self.title


class VillaServiceCategory(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'villa_service_categories'

    def __str__(self):
        return self.name


class VillaService(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(VillaServiceCategory, on_delete=models.CASCADE)
    villa = models.ManyToManyField('Villa', related_name='villas')


class Villa(models.Model):
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    d_center = models.PositiveIntegerField(null=True, blank=True)
    d_airways = models.PositiveIntegerField(null=True, blank=True)
    d_railways = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        db_table = 'villas'

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='news', blank=True, null=True)
    created = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'news'

    def __str__(self):
        return self.title
