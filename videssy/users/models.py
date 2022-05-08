"""User models have case case-insensitive usernames and emails
this is good because this way, no two usernames can be the same at all.
This leads to completely unique usernames to be made."""
import uuid

from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.db import models

from vlog.models import Video


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
    """
    CICharField makes sure that input is 
    case-insensitive
    """
    username = CICharField(unique=True, max_length=20)
    email = CIEmailField(unique=True,max_length=150)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    liked_videos = models.ManyToManyField(Video, blank=True)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
