from django.urls import path

from .views import Mailings

urlpatterns = [
    path('', Mailings.as_view(), name='mailings'),
    ]