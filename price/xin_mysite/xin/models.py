from django.db import models


class XinCar(models.Model):
    name = models.CharField(max_length=512)
    city = models.CharField(max_length=512)
    price = models.CharField(max_length=512)
    licensed_time = models.CharField(max_length=512)
    mile = models.CharField(max_length=512)
