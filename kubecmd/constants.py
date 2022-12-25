import enum


@enum.unique
class BuildStatus(enum.Enum):
    NOT_STARTED = 1
    IN_PROGRESS = 2
    FAILED = 3
    COMPLETED = 4


@enum.unique
class KubeKindComponentName(enum.Enum):
    CONFIG_MAP = 'ConfigMap'
    DEPLOYMENT = 'Deployment'
    SERVICE = 'Service'
    INGRESS = 'Ingress'
    PERSISTENT_VOLUME_CLAIM = 'PersistentVolumeClaim'


@enum.unique
class SystemTypeApplication(enum.Enum):
    mysql_5_7 = 'mysql_5_7'
    wordpress_6_0 = 'wordpress_6_0'
