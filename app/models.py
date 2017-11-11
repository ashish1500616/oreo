from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils import timezone

from django.contrib.auth.models import User

class Login(models.Model):
    username = models.CharField(max_length=20)

    def __unicode__(self):
        return self.username


class User_detail(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField(max_length=264, unique=True)

    def __unicode__(self):
        return self.firstname




class Image(models.Model):

    img_1_a = models.URLField(blank=True)
    img_1_b = models.URLField(blank=True)
    img_2_a = models.URLField(blank=True)
    img_2_b = models.URLField(blank=True)
    img_3_a = models.URLField(blank=True)
    img_3_b = models.URLField(blank=True)

    # def __str__(self):
    #     return str(self.id)