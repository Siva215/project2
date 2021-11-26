from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def siva(request):
    return HttpResponse("<h1>This is Application</h1>")