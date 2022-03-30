"""
Methods to insert and query database

Requirements: data base existst
"""

from datetime import datetime as dt
from postgrestry.models import Sign


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

    try: 
        res = all.get(hackernews_username=username)
        print("found, gem id:", res.gem_id) # debug
        return True
    except: 
        print("not found")    # debug
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
