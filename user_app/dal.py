
from user_app import models


def get_application_by_id(id: int) -> models.UserApplication:
    try:
        return models.UserApplication.objects.get(pk=id)
    except models.UserApplication.DoesNotExist:
        return


def get_application_by_name(name: str) -> models.UserApplication:
    try:
        return models.UserApplication.objects.get(name=name)
    except models.UserApplication.DoesNotExist:
        return
