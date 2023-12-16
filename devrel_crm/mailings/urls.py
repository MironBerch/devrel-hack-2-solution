from django.urls import path

from mailings.views import Mailings

urlpatterns = [
    path('', Mailings.as_view(), name='mailings'),
]
