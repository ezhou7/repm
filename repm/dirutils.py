import os


def init_sub_directory(dir_name):
    if not os.path.exists(dir_name):
        print("Creating {} sub-directory...".format(dir_name))
        os.mkdir(dir_name)
        print("Created {} sub-directory".format(dir_name))
    else:
        print("Cannot create /{0} sub-directory; /{0} already exists".format(dir_name))


def get_repm_project_root_directory():
    cwd = os.path.abspath(os.getcwd())
    while cwd != "/":
        cwd = os.path.abspath(os.path.join(cwd, os.pardir))
        in_repm_project = any(os.path.basename(file) == "/.repm" for file in os.listdir(cwd))
        if in_repm_project:
            return cwd

    return None