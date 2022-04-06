from django.urls import path

from api.v1 import views

urlpatterns = [
    path('qr/', views.get_banana)
]