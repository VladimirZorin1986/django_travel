from django.shortcuts import render


def hello(request):
    name = 'Vladimir'
    return render(request, 'hello.html', {'name': name})


def about(request):
    string = 'About us'
    return render(request, 'about.html', {'string': string})
