from typing import Union
from uuid import UUID

from rest_framework.request import Request

from base.models import Vehicle
from api.v1.serializers import VehicleSerializer


class BaseModel:

    @classmethod
    def get_all_instances(cls) -> dict:
        return cls.serialize(Vehicle.objects.all(), many=True)

    @classmethod
    def find_by_id(cls, id: UUID) -> Union[list, 'Vehicle']:
        result = Vehicle.objects.filter(id=id)
        return [] if not result else list(result)[0]

    @classmethod
    def serialize(cls, instance: 'Vehicle', many: bool) -> dict:
        return VehicleSerializer(instance, many=many).data

    @classmethod
    def update_fields(cls, instance: 'Vehicle', request: Request) -> 'Vehicle':
        request = request.data
        instance.type = request['type']
        # Add more vehicle params when data model is approved
        return instance
