
from django.db import models

from account import constants
from common import models as common_models
# Create your models here.

class SocialMediaUser(common_models.BaseModel):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    social_login_type = models.IntegerField(choices=constants.SOCIAL_LOGIN_IDS)
    social_login_user_id = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        unique_together = (
            ('user', 'social_login_type')
        )
