import os
from typing import Optional


def init_sub_directory(dir_name: str):
    if not os.path.exists(dir_name):
        print("Creating {} sub-directory...".format(dir_name))
        os.mkdir(dir_name)
        print("Created {} sub-directory".format(dir_name))
    else:
        print("Cannot create /{0} sub-directory; /{0} already exists".format(dir_name))


def get_repm_project_root_directory() -> Optional[str]:
    cwd: str = os.path.abspath(os.getcwd())
    while cwd != "/":
        in_repm_project = any(os.path.basename(file) == ".repm.json" for file in os.listdir(cwd))
        if in_repm_project:
            return cwd

        cwd = os.path.abspath(os.path.join(cwd, os.pardir))

    return None
