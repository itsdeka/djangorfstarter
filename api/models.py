from django.db import models
from django.db.models.query import QuerySet
from django.db.models.signals import post_save, pre_save, post_delete, pre_delete
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.template.defaultfilters import slugify

from datetime import datetime, time, timedelta
from dateutil import tz

import api.utilities as utilities

class User(AbstractUser):

    def __str__(self):
        return f'{self.email}'

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-id']

