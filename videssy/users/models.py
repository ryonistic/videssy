"""User models have case case-insensitive usernames and emails
this is good because this way, no two usernames can be the same at all.
By default, django allows usernames like Alex and alex to be considered different,
but that can cause confusion so i made it so that both usernames will be the same. 
Anyone who tries to create a username 'alex' when 'Alex' already exists, will be told 
that they cant do it because a similar enough username exists already, same goes for email. 
This leads to completely unique usernames to be made."""
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class CaseInsensitiveFieldMixin:
    """
    Field mixin that uses case-insensitive lookup alternatives if they exist.
    """
    LOOKUP_CONVERSIONS = {
        'exact': 'iexact',
        'contains': 'icontains',
        'startswith': 'istartswith',
        'endswith': 'iendswith',
        'regex': 'iregex',
    }
    def get_lookup(self, lookup_name):
        converted = self.LOOKUP_CONVERSIONS.get(lookup_name, lookup_name)
        return super().get_lookup(converted)


class CICharField(CaseInsensitiveFieldMixin, models.CharField):
    pass

class CIEmailField(CaseInsensitiveFieldMixin, models.EmailField):
    pass


class User(AbstractUser):
    username = CICharField(unique=True, max_length=20)
    email = CIEmailField(unique=True,max_length=150)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
