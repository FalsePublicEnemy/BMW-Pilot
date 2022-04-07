from typing import Union
from uuid import UUID

from rest_framework.request import Request


class BaseModel:

    @classmethod
    def get_all_instances(cls) -> dict:
        return cls.objects.all()

    @classmethod
    def find_by_id(cls, id: UUID):
        result = cls.objects.filter(id=id)
        return [] if not result else list(result)[0]

    @classmethod
    def update_fields(cls, instance: '...', request: Request) -> '...':
        request = request.data
        instance.type = request['type']
        # Add more vehicle params when data model is approved
        return instance
