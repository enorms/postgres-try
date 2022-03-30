from django.shortcuts import render
from datetime import datetime as dt

from postgrestry.models import Sign
from postgrestry.dbmanager import query_discord_username

# Create your views here.
def index(request):
    return print("views > index()")

to_search = "dis_un2"
def db(request):
    """
    res = all.filter(hackernews_username="hn_un2") # query set
    res = all.get(hackernews_username="hn_un2") # Sign object
    res.gem_id  # 29
    """
    seconds = dt.now().second
    sign = Sign(gem_id = seconds, hackernews_username="hn_un", discord_username="dis_un", wallet_address="0x345555",message_payload={"test_key":"test_value"})
    sign.save()

    print(sign) # debug

    signs = Sign.objects.all()

    return render(request, "db.html", {"signs": signs})
    

def db_with_param(request, username):
    """
    test whether we can call this via API
    """
    print("db_with_param(), username:", username) # debug
    
    res = query_discord_username(username)
    
    print(res) # debug

    return render(request, "username.html", {"found": res})
    