
import yaml
from string import Template

from common import public as common_public
from kubecmd import constants as kube_cmd_constants
from kubecmd import public as kubecmd_public
from kubecmd import utils as kubecmd_utils
from user_app import exceptions

get_random_word_of_varying_length = common_public.get_random_lower_case_word_of_varying_length


def deploy_wordpress_app(app_id: int, build_type: str = 'yaml'):
    """Setup for wordpress deployment"""

    if build_type != 'yaml':
        return

    system_app = kubecmd_public.get_system_application_by_id(app_id)
    if not system_app:
        raise exceptions.RecordNotFoundException()

    config = system_app.config or {}
    extra_config = system_app.extra_config or {}
    env_variables = []
    if extra_config and extra_config.get('type') == 'env':

        for app_type in extra_config.get('app_type_list'):
            env_from_app_type = None
            try:
                env_from_app_type = get_env_variables_from_app_deployment(app_type)
            except exceptions.UserApplicationNotFound as e:
                raise e

            if env_from_app_type:
                env_variables.extend(app_env for app_env in env_from_app_type)

    # CAUTION! : Eval to be used only by ADMIN
    for key in config:
        config[key] = eval(config[key])

    yaml_text = Template(system_app.build_instruction_yaml)
    yam_to_json_instructions = yaml.load_all(yaml_text.substitute(**config), yaml.FullLoader)
    kube_kind_names = kube_cmd_constants.KubeKindComponentName
    kube_kind_names = {
        kube_kind_names.PERSISTENT_VOLUME_CLAIM.value: _deploy_persistent_volume,
        kube_kind_names.INGRESS.value: _deploy_ingress,
        kube_kind_names.SERVICE.value: _deploy_service,
        kube_kind_names.DEPLOYMENT.value: _deploy_deployment
    }
    instruction_used = {}
    build_status = build_status = kube_cmd_constants.BuildStatus.COMPLETED.value
    reserved = False
    logs = None
    for instruction in yam_to_json_instructions:
        function_to_call = kube_kind_names.get(instruction['kind'])
        if not function_to_call:
            continue        

        instruction_used[instruction['kind']] = instruction
        result = function_to_call(instruction)
        if result is not None:
            build_status = kube_cmd_constants.BuildStatus.FAILED.value
            reserved = True
            logs = str(result)
            break

    kubecmd_public.set_systen_app_in_queue_with_name_and_type(
        app_name=config['name'],
        app_type=system_app.get_flattened_name(),
        system_app_id=system_app.id,
        instruction=instruction_used,
        build_status=build_status,
        reserved=reserved,
        logs=logs
    )


def get_env_variables_from_app_deployment(app_type: str):
    app_in_queue = kubecmd_public.get_system_application_in_queue_by_app_type(
        app_type=app_type
    )
    if not app_in_queue:
        raise exceptions.UserApplicationNotFound

    instruction_json = app_in_queue.instruction_json
    try:
        deployment = instruction_json['Deployment']
        return deployment['spec']['template']['spec']['containers'][0].get('env')
    except KeyError as e:
        raise e


def get_name_key_from_env_variable(env_variables: list, key_name: str):
    """Returns the value once the matching name is found."""

    for env_variable in env_variables:
        if env_variable['name'] == key_name:
            return env_variable['value']


def _deploy_ingress(ingress_body: dict):
    try:
        kubecmd_utils.networking_v1_api.create_namespaced_ingress(
            namespace='default', body=ingress_body
        )
    except Exception as e:
        # CAUTION : Raise alert 
        return e


def _deploy_service(service_body: dict):
    try:
        kubecmd_utils.core_v1_api.create_namespaced_service(
            namespace='default', body=service_body
        )
    except Exception as e:
        return e


def _deploy_persistent_volume(pvc_body: dict):
    try:
        kubecmd_utils.core_v1_api.create_namespaced_persistent_volume_claim(
            namespace='default', body=pvc_body
        )
    except Exception as e:
        return e


def _deploy_deployment(deployment_body: dict):
    try:
        kubecmd_utils.apps_v1_api.create_namespaced_deployment(
            namespace='default', body=deployment_body
        )
    except Exception as e:
        return e
