from uuid import UUID

from django.http import HttpResponseNotFound
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView

from api.v1.serializers import VehicleSerializer
from base.models import Vehicle


class VehicleResource(APIView):
    """Resource works with unique car instance"""

    @staticmethod
    def get(request: Request, uuid: UUID) -> Response(dict):
        """Get one car instance by UUID"""
        vehicle_raw = Vehicle.find_by_id(id=uuid)
        if not vehicle_raw:
            return HttpResponseNotFound('Car with this UUID is not found')
        response = {
            'data': Vehicle.serialize(vehicle_raw, False),
            'metadata': {
                'uuid': uuid,
            }
        }
        return Response(response)

    @staticmethod
    def patch(request: Request, uuid: UUID) -> Response(dict):
        """Update car instance with new data"""

        vehicle_raw = Vehicle.find_by_id(id=uuid)
        if not vehicle_raw:
            return HttpResponseNotFound('Car with this UUID is not found')

        vehicle_raw.update_fields(vehicle_raw, request)
        vehicle_raw.save()

        response = {
            'data': Vehicle.serialize(vehicle_raw, False),
            'metadata': {
                'uuid': uuid,
            }
        }
        return Response(response)


class VehicleEndpoint(APIView):
    """Endpoint works with all available car instances"""

    @staticmethod
    def get(request: Request):
        """Get list of available car instances"""
        response = Vehicle.get_all_instances()
        return Response(response)

    @staticmethod
    def post(request: Request):
        """Creates new car instance"""

        vehicle_raw = VehicleSerializer(data=request.data)
        if vehicle_raw.is_valid():
            vehicle_raw.save()


        response = {
                'action': 'created',
                'data': vehicle_raw.data,
        }

        return Response(response)
