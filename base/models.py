from uuid import uuid4

from django.db import models

from base.base_model import BaseModel


class Vehicle(models.Model, BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    # TODO: prove specs for car. What's needed to be shown in description


class Test(models.Model):
    name = models.CharField(max_length=100)


