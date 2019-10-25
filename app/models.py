from django.db import models

# Create your models here.


class Category(models.Model):
	name = models.CharField(max_length=255, null=True, blank=True)


class Facility(models.Model):
	name = models.CharField(max_length=255, null=True, blank=True)
	image = models.ImageField(upload_to='facilities', null=True, blank=True)
	tour = models.ForeignKey('Tour', on_delete=models.CASCADE)

class Expense(models.Model):
	name = models.CharField(max_length=255, null=True, blank=True)
	image = models.ImageField(upload_to='expenses', null=True, blank=True)


class Tour(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='tours', null=True, blank=True)
    route = models.CharField(max_length=255, null=True, blank=True)
    duration = models.PositiveIntegerField(null=True, blank=True)
    max_people = models.PositiveIntegerField(null=True, blank=True)
    guide = models.BooleanField(null=True, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)
    plan = models.TextField(null=True, blank=True)


class Sight(models.Model):
	title = models.CharField(max_length=255, null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	image = models.ImageField(upload_to='sights', null=True, blank=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
