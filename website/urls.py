from django.urls import path, re_path

from website.views import MainPage


urlpatterns = [
    path('', MainPage.home),
    path('/features', MainPage.features),
]
