# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.conf import settings


class SillyModel(models.Model):
    silly_field = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
