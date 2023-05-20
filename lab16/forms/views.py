from django.http import HttpResponse


def index(request):
    return HttpResponse("start lab 16")
