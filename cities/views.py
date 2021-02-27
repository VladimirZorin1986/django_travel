from django.shortcuts import render
from cities.models import City


def hello(request):
    qs = City.objects.all()
    context = {'cities_list': qs}
    return render(request, 'cities/home.html', context)
