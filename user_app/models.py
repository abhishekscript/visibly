from django.db import models

from common import models as common_models
# Create your models here.


class UserApplication(common_models.BaseModel):
    name = models.CharField(max_length=20)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    hostname = models.CharField(null=True, max_length=200)
    subhostname = models.CharField(max_length=30, unique=True)
    service = models.JSONField(null=True)
    ingress = models.JSONField(null=True)
    deployment = models.JSONField(null=True)
    replicas = models.PositiveSmallIntegerField(null=True, default=1)
    storage = models.PositiveSmallIntegerField(null=True)
    cpu = models.PositiveSmallIntegerField(null=True)
    active = models.BooleanField(default=False)
