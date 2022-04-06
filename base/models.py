from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
