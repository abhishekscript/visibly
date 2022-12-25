from kubernetes import client
from kubernetes import config

try:
    config.load_incluster_config()
except config.config_exception.ConfigException:
    config.load_kube_config()


core_v1_api = client.CoreV1Api()
apps_v1_api = client.AppsV1Api()
networking_v1_api = client.NetworkingV1Api()
