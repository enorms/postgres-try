from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import postgrestry.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", postgrestry.views.index, name="index"),
    path("db/", postgrestry.views.db, name="db"),
    path("db/<str:username>", postgrestry.views.db_with_param, name = "verify_discord_username"),
    path("admin/", admin.site.urls),
]
