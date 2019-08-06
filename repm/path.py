import os

from repm import RESOURCES_ROOT_DIR


def get_resources_item_path(item_name: str) -> str:
    item_path: str = os.path.join(RESOURCES_ROOT_DIR, item_name)
    if not os.path.exists(item_path):
        raise FileNotFoundError("Item {} not found".format(item_path))

    return item_path
