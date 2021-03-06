from django.contrib.postgres.fields import JSONField
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify

from adminka.tours.get_icons import Icons


class VillaImage(models.Model):
    image = models.ImageField(upload_to='villas', null=True, blank=True)
    villa = models.ForeignKey('Villa', on_delete=models.CASCADE)

    class Meta:
        db_table = 'villa_images'
        ordering = ['-id']

    def __str__(self):
        return self.image.name or 'asd'


class VillaServiceCategory(models.Model):
    title = JSONField()

    class Meta:
        db_table = 'villa_service_categories'
        ordering = ['-id']

    def __str__(self):
        return self.title['title_en'] or 'asd'


class VillaService(models.Model):
    title = JSONField()
    category = models.ForeignKey(VillaServiceCategory, on_delete=models.SET_NULL, null=True)
    villas = models.ManyToManyField('Villa', related_name='v_services')

    class Meta:
        db_table = 'villa_services'
        ordering = ['-id']

    def __str__(self):
        return self.title['title_en'] or 'asd'


STATUS = (
    (0, 'Signature villa'),
    (1, 'Garden home villa')
)


class Villa(models.Model):
    title = JSONField()
    address = JSONField(null=True)
    description = JSONField(null=True)
    slug = models.SlugField(max_length=255)
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
        return self.title['title_en'] or 'asd'


@receiver(post_save, sender=Villa)
def get_slug3(sender, instance, created, **kwargs):
    if created:
        slug = slugify(instance.title['title_en'])
        instance.slug = slug
        instance.save()
