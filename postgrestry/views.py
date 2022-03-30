import logging
from datetime import datetime as dt
from django.shortcuts import render

from postgrestry.models import Sign
from postgrestry.dbmanager import query_discord_username

# https://www.delftstack.com/howto/django/django-print-to-console/
logging.basicConfig(level=logging.DEBUG) 

# Create your views here.
def index(request):
    return print("views > index()")

to_search = "dis_un2"
hackernews_username = "hnid"
def db(request):
    """
    res = all.filter(hackernews_username="hn_un2") # query set
    res = all.get(hackernews_username="hn_un2") # Sign object
    res.gem_id  # 29
    """
    seconds = dt.now().second
    sign = Sign(gem_id = seconds, hackernews_username=hackernews_username, discord_username="dis_un", wallet_address="0x345555",message_payload={"test_key":"test_value"})
    sign.save()

    logging.debug(str(sign))

    signs = Sign.objects.all()

    return render(request, "db.html", {"signs": signs})
    

def username(request, username):
    """
    called from URLS with param passed
    runs code, then sends output to html template with vars
    test whether we can call this via API
    """
    logging.debug("username(), username:", str(username))
    
    result = query_discord_username(username)

    logging.debug(str(result))

    return render(request, "username.html", {"result": result})
    