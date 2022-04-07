from django.urls import path, re_path

from website import views


urlpatterns = [
    path('info/<uuid>', views.index)
]
