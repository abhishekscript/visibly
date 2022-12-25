from django.db import models
from django.http import request

from common import models as common_model
from common import constants as common_constant
from stocks import constants

# Create your models here.
class Equity(common_model.BaseModel):
    security_id = models.CharField(max_length=50, null=False, blank=False)
    security_code = models.IntegerField(unique=True, db_index=True)
    security_name = models.CharField(max_length=100, null=False, blank=False)
    issuer_name = models.CharField(max_length=100, null=False, blank=False)
    status = models.PositiveSmallIntegerField(
        choices=common_constant.STATUS_MAP, null=False
    )
    group = models.PositiveSmallIntegerField(choices=constants.ASSET_GROUP, null=False)
    face_value = models.FloatField( null=False)
    industry = models.CharField(max_length=100, null=False, blank=False)
    sector_name = models.CharField(max_length=100, null=False, blank=False)
    group_name = models.CharField(max_length=100, null=False, blank=False)
    sub_group_name = models.CharField(max_length=100, null=False, blank=False)
    isin_number = models.CharField(max_length=20, null=False, blank=False)
