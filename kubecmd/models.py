
from django.core.exceptions import ValidationError
from django.db import models

from common import models as common_models
from kubecmd import constants
# Create your models here.


class SystemApplication(common_models.BaseModel):
    name = models.CharField(max_length=30)
    version = models.FloatField(default=0.1)
    build_instruction_json = models.JSONField(null=True, blank=True)
    build_instruction_yaml = models.TextField(null=True, blank=True)
    build_status = models.PositiveSmallIntegerField(
        default=1, choices=common_models.enum_to_choices(constants.BuildStatus), null=False
    )
    config = models.JSONField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    extra_config = models.JSONField(null=True, blank=True)

    class Meta:
        unique_together = ('name', 'version')

    def clean(self):
        if not (self.build_instruction_json or self.build_instruction_yaml):
            raise ValidationError('build instruction required in json `OR` yaml format')

    def save(self, *args, **kwargs):
        self.clean()
        super(SystemApplication, self).save(*args, **kwargs)
    
    def get_flattened_name(self):
        return self.name + '_' + str(self.version).replace('.', '_')

    def __str__(self):
        return str(self.id) + ': ' +self.name


class SystemApplicationConfig(common_models.BaseModel):
    system_application = models.ForeignKey(SystemApplication, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    config = models.JSONField(null=False)
    config_text = models.TextField(null=False)

    class Meta:
        unique_together = ('system_application', 'name')


class SystemApplicationInQueue(common_models.BaseModel):
    name = models.CharField(max_length=20, unique=True)
    reserved = models.BooleanField(default=True)
    app_type = models.CharField(
        choices=common_models.enum_to_choices(constants.SystemTypeApplication),
        db_index=True,
        max_length=30
    )
    system_application = models.ForeignKey(SystemApplication, on_delete=models.CASCADE)
    instruction_json = models.JSONField(null=True)
    instruction_yaml = models.TextField(null=True)
    logs = models.TextField(null=True, blank=True)
    build_status = models.PositiveSmallIntegerField(
        default=1, choices=common_models.enum_to_choices(constants.BuildStatus), null=False
    )


class StandAloneSystemApplication(common_models.BaseModel):
    is_active = models.BooleanField(default=False)
    #system_application = models.One