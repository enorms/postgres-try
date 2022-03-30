import os
import requests
from django.shortcuts import render
from django.http import HttpResponse

from .models import Sign

# Create your views here.
def index(request):
    return print("views > index()")

i = 1
def db(request):
    i+=1
    sign = Sign(gem_id = i, hackernews_username="hn_un", discord_username="dis_un", wallet_address="0x345555",message_payload={"test_key":"test_value"})
    sign.save()

    sign = Sign.objects.all()

    return render(request, "db.html", {"sign": sign})
    
