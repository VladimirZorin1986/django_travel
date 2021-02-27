from django.urls import path
from cities.views import hello

urlpatterns = [
    path('', hello),
]
