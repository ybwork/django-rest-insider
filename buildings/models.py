from django.db import models

from companies.models import Company


class Building(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='')
    region = models.CharField(max_length=100, blank=True, default='')
    district = models.CharField(max_length=100, blank=True, default='')
    city = models.CharField(max_length=50, blank=True, default='')
    country = models.CharField(max_length=100, blank=True, default='')
    images = models.TextField(blank=True, default='')
    video = models.TextField(blank=True, default='')
    coordinates = models.TextField(blank=True, default='')
    currency = models.CharField(max_length=50, blank=True, default='')

    class Meta:
        ordering = ['id']