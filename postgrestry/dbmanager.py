"""
Methods to insert and query database

Requirements: data base existst
"""
import logging
from datetime import datetime as dt
from postgrestry.models import Sign


# https://www.delftstack.com/howto/django/django-print-to-console/
logging.basicConfig(level=logging.DEBUG) 


def save_record(record):
    """
    record should be a dictionay object with items in Sign objects class

    res = all.filter(hackernews_username="hn_un2") # query set
    res = all.get(hackernews_username="hn_un2") # Sign object
    res.gem_id  # 29
    """
    seconds = dt.now().second
    sign = Sign(gem_id = record.get('gem_id'),
                hackernews_username = record.get('hackernews_username'),
                discord_username = record.get('discord_username'),
                wallet_address = record.get('wallet_address'),
                message_payload = record.get ('message_payload'))
    sign.save()

    print(query_discord_username(record.get('hackernews_username'))) # debug; expect True

    return 


def query_discord_username(username):
    """Given a username
    return true if associated with a record containing a gem_id
    
    Example of code return if not found:
        postgrestry.models.Sign.DoesNotExist: Sign matching query does not exist.
    """
    logging.debug("query_discord_username(), username:", username)


    try: 
        all = Sign.objects.all()
        res = all.get(hackernews_username=username)
        logging.debug("found, gem id:", str(res.gem_id))
        return True
    except: 
        logging.debug("not found")
        return False


def test_dbmanager():
    """
    Good and bad records for testing.
    """
    seconds = dt.now().second

    # expect true
    sign = Sign(gem_id = seconds, 
                hackernews_username="hn_un", 
                discord_username="dis_un", 
                wallet_address="0x345555", 
                message_payload={"test_key":"test_value"})

    # expect false
    ## repeat
    sign = Sign(gem_id = seconds,
                hackernews_username="hn_un",
                discord_username="dis_un",
                wallet_address="0x345555", 
                message_payload={"test_key":"test_value"})
    
    ## missing data
    sign = Sign(gem_id = seconds, 
                hackernews_username="", 
                discord_username="", 
                wallet_address="0x345555",
                message_payload={"test_key":"test_value"})

    ### bad wallet
    sign = Sign(gem_id = seconds, 
                hackernews_username="", 
                discord_username="", 
                wallet_address="!!!", 
                message_payload={"test_key":"test_value"})
