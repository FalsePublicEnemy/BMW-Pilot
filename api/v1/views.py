from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.v1.serializers import CarSerializer
from base.models import Car


@api_view(['GET', 'POST'])
def get_banana(request):
    if request.method == 'GET':
        items = Car.objects.all()
        cars = CarSerializer(items, many=True)
        return Response(cars.data)
    elif request.method == 'POST':
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
    return Response()
