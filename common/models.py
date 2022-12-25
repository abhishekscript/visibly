from django.db import models
from django.utils import timezone

# Create your models here.

def tz_now():
    return timezone.now()


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(default=tz_now)
    updated_at = models.DateTimeField(auto_now=True)


class NoUpdateBaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(default=tz_now)


def enum_to_choices(enum):
    return tuple(
        [(choice.value, choice.name.replace('_', ' ').title()) for choice in enum]
    )
