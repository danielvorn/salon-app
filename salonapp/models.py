from django.db import models


class Salon(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
