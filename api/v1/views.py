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
        vehicle = Vehicle.objects.filter(id=uuid)
        if not vehicle:
            return HttpResponseNotFound('Car with this UUID is not found')
        response = {
            'data': VehicleSerializer(list(vehicle)[0], many=False).data,
            'metadata': {
                'uuid': uuid,
            }
        }

        return Response(response)

    @staticmethod
    def patch(request: Request, uuid: UUID) -> Response(dict):
        """Update car instance with new data"""

        vehicle = list(Vehicle.objects.filter(id=uuid))[0]
        if not vehicle:
            return HttpResponseNotFound('Car with this UUID is not found')

        vehicle.update_fields(
            obj=vehicle,
            request=request,
        )
        vehicle.save()

        response = {
            'data': VehicleSerializer(vehicle, many=False).data,
            'metadata': {
                'uuid': uuid,
            }
        }

        # TODO: patch doesn't working. Need to fix

        return Response(response)


class VehicleEndpoint(APIView):
    """Endpoint works with all available car instances"""

    @staticmethod
    def get(request: Request):
        """Get list of available car instances"""
        items = Vehicle.objects.all()
        cars = VehicleSerializer(items, many=True)
        return Response(cars.data)

    @staticmethod
    def post(request: Request):
        """Creates new car instance"""

        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(
            {
                'action': 'created',
                'data': serializer.data,
            }
        )
