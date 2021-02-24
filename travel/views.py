from django.shortcuts import render


def hello(request):
    name = 'Vladimir'
    return render(request, 'hello.html', {'name': name})
