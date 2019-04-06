import os


def init_sub_directory(dir_name):
    if not os.path.exists(dir_name):
        print("Creating {} sub-directory...".format(dir_name))
        os.mkdir(dir_name)
        print("Created {} sub-directory".format(dir_name))
    else:
        print("Cannot create /{0} sub-directory; /{0} already exists".format(dir_name))
