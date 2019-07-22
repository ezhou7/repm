import os
from sh import git

from repm.dirutils import init_sub_directory
from repm.package import Setup


def create_new_research_project(project_name):
    create_project_directory(project_name)

    init_project_directory_with_git()
    init_project_directory_with_gitignore(project_name)
    init_project_directory_with_setup_py(project_name)
    init_project_directory_with_repm_file()
    init_project_directory_with_data_sub_directory()
    init_project_directory_with_config_sub_directory()
    init_project_directory_with_resources_sub_directory()
    init_project_directory_with_artifacts_sub_directory()

    commit_project_directory()


def create_project_directory(project_name):
    project_dir_path = os.path.abspath("./{}/".format(project_name))
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
        fin.write("artifacts\n")
        fin.write("{}.egg-info\n".format(project_name))
        fin.write("**/__pycache__/\n")
        fin.write(".repm.json")


def init_project_directory_with_setup_py(project_name):
    # initialize the new project directory with setup.py
    with open("setup.py", "w") as fin:
        fin.write(str(Setup(project_name)))


def init_project_directory_with_repm_file():
    # initialize the new project directory with a .repm file
    with open(".repm.json", "w") as fin:
        fin.write("{}\n")


def init_project_directory_with_data_sub_directory():
    # initialize the new project directory with a data sub-directory
    init_sub_directory("data")


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
    init_sub_directory("resources")


def init_project_directory_with_artifacts_sub_directory():
    # initialize the new project directory with an artifacts (saved models) sub-directory
    init_sub_directory("artifacts")


def commit_project_directory():
    print("Committing all created files and directories...")
    git.add(".")
    git.commit("-m", "\"Initial commit by repm\"")
    print("Committed initial commit")
