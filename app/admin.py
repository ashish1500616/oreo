from django.contrib import admin

# Register your models here.

from .models import Image #UserProfileInfo
admin.site.register(Image)
# admin.site.register(UserProfileInfo)
