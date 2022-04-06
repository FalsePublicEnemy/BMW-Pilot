import uuid

from django.urls import path, re_path

from api.v1.views import VehicleResource
from api.v1.views import VehicleEndpoint

urlpatterns = [
    path('vehicle/<uuid>', VehicleResource.as_view()),
    path('vehicle', VehicleEndpoint.as_view()),
]

