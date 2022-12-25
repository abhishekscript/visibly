
from kubecmd import models


def get_application_by_id(id: int) -> models.SystemApplication:
    try:
        return models.SystemApplication.objects.get(pk=id)
    except models.SystemApplication.DoesNotExist:
        return


def get_application_with_config(fk: int) -> models.SystemApplicationConfig:
    try:
        return models.SystemApplicationConfig.objects.get(system_application_id=fk)
    except models.SystemApplicationConfig.DoesNotExist:
        return


def get_system_application_in_queue_by_app_type(app_type: str):
    """Returns recently App from queue based on app_type."""

    app_in_queue = models.SystemApplicationInQueue.objects.filter(app_type=app_type, reserved=False).first()
    if not app_in_queue:
        return

    app_in_queue.reserved = True
    app_in_queue.save()
    return app_in_queue


def set_app_name_and_type_for_system_application_in_queue(
    app_name: str, app_type: str, system_app_id: int, instruction: dict, build_status: int, reserved: bool, logs: str
):
    """Creates system application in queue with name, app_type and instruction."""

    return models.SystemApplicationInQueue.objects.create(
        name=app_name,
        app_type=app_type,
        system_application_id=system_app_id,
        instruction_json=instruction,
        build_status=build_status,
        reserved=reserved,
        logs=logs
    )
