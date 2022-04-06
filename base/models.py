import uuid

from django.db import models


class Vehicle(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    # TODO: prove specs for car. What's needed to be shown in description

