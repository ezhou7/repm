import os


CODE_PACKAGE_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

RESOURCES_ROOT_DIR = os.path.join(CODE_PACKAGE_ROOT_DIR, "resources")

SERVER_API_URL = "https://repm.io/api"


def get_api_url(api_path: str):
    return SERVER_API_URL + api_path \
        if api_path.startswith("/") \
        else "{}/{}".format(SERVER_API_URL, api_path)
