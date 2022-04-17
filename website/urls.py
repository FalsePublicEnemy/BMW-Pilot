from django.conf import settings
from django.urls import path, re_path
from django.conf.urls.static import static


from website.views import MainPage


urlpatterns = [
    path('', MainPage.home),
    path('features', MainPage.features),
] + static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
