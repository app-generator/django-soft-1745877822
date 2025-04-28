# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Store(models.Model):

    #__Store_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    address = models.TextField(max_length=255, null=True, blank=True)
    email = models.TextField(max_length=255, null=True, blank=True)
    latitude = models.TextField(max_length=255, null=True, blank=True)
    longitude = models.TextField(max_length=255, null=True, blank=True)

    #__Store_FIELDS__END

    class Meta:
        verbose_name        = _("Store")
        verbose_name_plural = _("Store")


class Display(models.Model):

    #__Display_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)
    heigth = models.IntegerField(null=True, blank=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    #__Display_FIELDS__END

    class Meta:
        verbose_name        = _("Display")
        verbose_name_plural = _("Display")



#__MODELS__END
