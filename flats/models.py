from django.db import models
from django.db.models import PositiveIntegerField, IntegerField, CharField

from houses.models import House


class Flat(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    # schema = models.ImageField()
    price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
    number = PositiveIntegerField(db_index=True)
    entrance = PositiveIntegerField(db_index=True)
    floor = PositiveIntegerField(db_index=True)
    status = IntegerField(db_index=True)
    # clone_for_flats = CharField(max_length=255, blank=True, null=True, default='')
    type = CharField(max_length=255)

    class Meta:
        ordering = ['id']
