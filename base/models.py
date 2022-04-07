from typing import Tuple
import uuid

from django.db import models
from rest_framework.request import Request

from base.enums import VehicleParams


class Vehicle(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    # TODO: prove specs for car. What's needed to be shown in description

    @staticmethod
    def update_fields(obj: 'Vehicle', request: Request) -> 'Vehicle':
        request = request.data
        obj.type = request['type']
        # Add more vehicle params when data model is approved
        return obj
