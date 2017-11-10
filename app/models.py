from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils import timezone


class Image(models.Model):

    img_1_a = models.ImageField(blank=True)
    img_1_b = models.ImageField(blank=True)
    img_two_a = models.ImageField(blank=True)
    img_two_b = models.ImageField(blank=True)
    img_3_a = models.ImageField(blank=True)
    img_3_b = models.ImageField(blank=True)