import os
from pathlib import Path


CODE_PACKAGE_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

RESOURCES_ROOT_DIR = os.path.join(CODE_PACKAGE_ROOT_DIR, "resources")

GLOBAL_REPM_DIR = os.path.join(str(Path.home()), ".repm")


def get_global_file_path(relative_file_path: str):
    if not os.path.exists(GLOBAL_REPM_DIR):
        os.mkdir(GLOBAL_REPM_DIR)

    return os.path.join(GLOBAL_REPM_DIR, relative_file_path)


SERVER_API_URL = "https://repm.io/api"


def get_api_url(api_path: str):
    return SERVER_API_URL + api_path \
        if api_path.startswith("/") \
        else "{}/{}".format(SERVER_API_URL, api_path)
