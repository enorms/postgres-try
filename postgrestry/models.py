from django.db import models

# Create your models here.
class Greeting(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    hackernews_username = models.CharField(max_length=60),
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)

