from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from api.v1.serializers import CarSerializer
from base.models import Car


class CarView(APIView):

    @staticmethod
    def get(request):
        items = Car.objects.all()
        cars = CarSerializer(items, many=True)
        return Response(cars.data)

    @staticmethod
    def post(request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response()


def index(request):
    # Render the HTML template index.html with the data in the context variable
    return render(request, '/Users/karimnassar/Desktop/BMW/static/start.html', )
