import os
import requests
from django.shortcuts import render
from django.http import HttpResponse

from .models import Sign

# Create your views here.
def index(request):
    r = requests.get('https://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')

def db(request):

    sign = Sign()
    sign.save()

    sign = Sign.objects.all()

    return render(request, "db.html", {"sign": sign})
