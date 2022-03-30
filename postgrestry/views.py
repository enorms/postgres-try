import os
import requests
from django.shortcuts import render
from django.http import HttpResponse

from .models import Sign

# Create your views here.
def index(request):
    return print("views > index()")

def db(request):

    sign = Sign()
    sign.save()

    sign = Sign.objects.all()

    return render(request, "db.html", {"sign": sign})
    
