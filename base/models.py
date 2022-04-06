from django.db import models


class Car(models.Model):
    brand = models.CharField(default='BMW', max_length=100)
    # model = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
