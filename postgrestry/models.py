from django.db import models

# Create your models here.
# discord-config has 3 fields: id (UUID), created_at (timestamptz), config (JSON-B)
# sign-the-charter has 7 fields: id, created_at, gem_id (int2), hackernews_username, discord_username, wallet_address, message_payload (JSON-B)

# https://docs.djangoproject.com/en/4.0/ref/models/fields/
# https://www.postgresql.org/docs/8.1/datatype.html
"""
sign = Sign(gem_id = 1, hackernews_username="hn_un", discord_username="dis_un", wallet_address="0x345555",message_payload={"test_key":"test_value"}  )
"""
class Sign(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    created_at = models.DateTimeField(auto_now_add=True)
    gem_id = models.PositiveSmallIntegerField()
    hackernews_username = models.CharField(max_length=100)
    discord_username = models.CharField(max_length=100)
    wallet_address = models.CharField(max_length=100)
    message_payload = models.JSONField() # JSONField uses jsonb

