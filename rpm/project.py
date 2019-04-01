import os
from sh import git


def create_new_research_project(workspace_path, project_name):
    # ask user to set a default directory (optional)
    create_default_directory()
    # create/set a project directory
    create_project_directory(workspace_path, project_name)

    # set up project directory with git
    init_project_directory_with_git()
    # set up project directory with .gitignore
    init_project_directory_with_gitignore(project_name)
    # set up project directory with setup.py
    init_project_directory_with_setup_py(project_name)
    # set up project directory with data directory
    init_project_directory_with_data_sub_directory()
    # set up project directory with config/props directory
    init_project_directory_with_config_sub_directory()
    # set up project directory with resources directory
    init_project_directory_with_resources_sub_directory()

    # commit initial setup
    commit_template()


def create_default_directory():
    # TODO: implement this method
    # ask user to set a default directory (optional)
    pass


def create_project_directory(workspace_path, project_name):
    project_dir_path = os.path.abspath("{}/{}/".format(workspace_path, project_name))
    # initialize the new project directory
    if not os.path.exists(project_dir_path):
        print("Creating project {}...".format(project_dir_path))
        os.mkdir(project_dir_path)
        print("Created project {}".format(project_dir_path))
    else:
        print("Cannot create project {0}; directory {0} already exists".format(project_dir_path))

    os.chdir(project_dir_path)


def init_project_directory_with_git():
    # initialize the new project directory with git
    git.init()


def init_project_directory_with_gitignore(project_name):
    # initialize the new project directory with .gitignore file
    with open(".gitignore", "w") as fin:
        fin.write("build\n")
        fin.write("dist\n")
        fin.write("data\n")
        fin.write("resources\n")
        fin.write("{}.egg-info\n".format(project_name))
        fin.write("**/__pycache__/\n")


def init_project_directory_with_setup_py(project_name):
    # initialize the new project directory with setup.py
    with open("setup.py", "w") as fin:
        fin.write("from setuptools import setup, find_packages\n")
        fin.write("\n\n")

        fin.write("def setup_package():\n")
        fin.write("\tmetadata = dict(\n")
        fin.write("\t\tname=\"{}\",\n".format(project_name))
        fin.write("\t\tversion=\"1.0.0\",\n")
        fin.write("\t\tdescription=\"{}\",\n".format(project_name))
        fin.write("\t\tpackages=find_packages(),\n")
        fin.write("\t\tinstall_requires=[]\n")
        fin.write("\t)\n")
        fin.write("\n")
        fin.write("\tsetup(**metadata)\n")
        fin.write("\n\n")

        fin.write("if __name__ == \"__main__\":\n")
        fin.write("\tsetup_package()\n")


def init_project_directory_with_data_sub_directory():
    # initialize the new project directory with a data sub-directory
    data_dir = "data"
    if not os.path.exists(data_dir):
        print("Creating data directory...")
        os.mkdir(data_dir)
        print("Created data directory")
    else:
        print("Cannot create /data directory; /data already exists")


def init_project_directory_with_config_sub_directory():
    # initialize the new project directory with a config sub-directory
    config_dir = "config"
    if not os.path.exists(config_dir):
        print("Creating config directory...")
        os.mkdir(config_dir)
        os.chdir(config_dir)
        with open(".gitkeep", "w") as fin:
            pass
        os.chdir("../")
        print("Created config directory")
    else:
        print("Cannot create /config directory; /config already exists")


def init_project_directory_with_resources_sub_directory():
    # initialize the new project directory with a resources sub-directory
    resources_dir = "resources"
    if not os.path.exists(resources_dir):
        print("Creating resources directory...")
        os.mkdir(resources_dir)
        print("Created resources directory")
    else:
        print("Cannot create /resources directory; /resources already exists")


def commit_template():
    print("Committing all created files and directories...")
    git.add(".")
    git.commit("-m", "\"Initial commit by RPM\"")
    print("Committed initial commit")
