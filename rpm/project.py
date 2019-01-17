import os
from sh import git


def create_new_research_project():
    # TODO: implement this method
    # ask user to set a default directory (optional)
    # ask user to create/set a project directory
    # set up project directory with git and .gitignore
    # set up project directory with setup.py
    # set up project directory with data directory
    # set up project directory with config/props directory
    # set up project directory with resources directory
    pass


def create_default_directory():
    # TODO: implement this method
    # ask user to set a default directory (optional)
    pass


def create_project_directory(project_name):
    # initialize the new project directory
    if not os.path.exists(project_name):
        print("Creating project {}...".format(project_name))
        os.mkdir(project_name)
        print("Created project {}".format(project_name))
    else:
        print("Cannot create project {0}; directory {0} already exists".format(project_name))

    os.chdir(project_name)


def init_project_directory_with_git():
    # initialize the new project directory with git
    git.init()


def init_project_directory_with_setup_py(project_name):
    # initialize the new project directory with setup.py
    with open("setup.py", "w") as fin:
        fin.write("from setuptools import setup, find_packages\n")
        fin.write("\n\n")

        fin.write("def setup_package:\n")
        fin.write("\tmetadata = dict(\n")
        fin.write("\t\tname=\"{}\",\n".format(project_name))
        fin.write("\t\tversion=\"1.0.0\",\n")
        fin.write("\t\tdescription=\"{}\",\n".format(project_name))
        fin.write("\t\tpackages=\"find_packages()\",\n")
        fin.write("\t\tinstall_requires=[]\n")
        fin.write(")\n")
        fin.write("\n")
        fin.write("setup(**metadata)")
        fin.write("\n\n")

        fin.write("if __name__ == \"__main__\":\n")
        fin.write("\tsetup_package()\n")


def init_project_directory_with_data_sub_directory():
    # TODO: implement this method
    # initialize the new project directory with a data sub-directory
    pass


def init_project_directory_with_config_sub_directory():
    # TODO: implement this method
    # initialize the new project directory with a config sub-directory
    pass


def init_project_directory_with_resources_sub_directory():
    # TODO: implement this method
    # initialize the new project directory with a resources sub-directory
    pass
