from django.urls import path

from api.v1 import views

urlpatterns = [
    path('qr/', views.CarView.as_view()),
    path('test/', views.index, name='index'),
]
