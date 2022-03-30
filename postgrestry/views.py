import os
import requests
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime as dt

from .models import Sign

# Create your views here.
def index(request):
    return print("views > index()")

def db(request):
    seconds = dt.now().second
    sign = Sign(gem_id = seconds, hackernews_username="hn_un", discord_username="dis_un", wallet_address="0x345555",message_payload={"test_key":"test_value"})
    sign.save()

    print(sign) # debug

    signs = Sign.objects.all()

    return render(request, "db.html", {"signs": signs})
    
