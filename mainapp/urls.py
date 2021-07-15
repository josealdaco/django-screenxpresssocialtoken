from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from .views import *
# Create your tests here.
urlpatterns = [
    path('', views.mainapp, name="main"),
    path('data/send', views.send_token, name="send_token")



]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
