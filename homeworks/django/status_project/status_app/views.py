import random

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def status_view(request):
    return HttpResponse("OK")

def random_color(request):
    color = lambda: random.randint(0,255)
    return HttpResponse("#%02X%02X%02X" % (color(),color(),color()))