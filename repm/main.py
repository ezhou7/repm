import os
import argparse
from repm.project import create_new_research_project
from repm.download import download_dataset
from repm.upload import upload_dataset
from repm.auth import login, logout, signup


def main():
    arg_parser = argparse.ArgumentParser()

    # main arguments
    arg_parser.add_argument("-i", "--init", help="Initialize current directory as a new research project",
                            nargs="?", action=InitAction)
    arg_parser.add_argument("-l", "--login", help="Login with a username and password", nargs=0, action=LoginAction)
    arg_parser.add_argument("-o", "--logout", help="Logout of a session", nargs=0, action=LogoutAction)
    arg_parser.add_argument("-s", "--signup", help="Signup with a username and password", nargs=0, action=SignupAction)

    sub_parsers = arg_parser.add_subparsers()

    # main arguments w/ sub commands
    download_arg_parser = sub_parsers.add_parser("download")
    download_arg_parser.add_argument("-a", "--dataset", help="Download the dataset from a project", nargs=1,
                                     action=DownloadDatasetAction)
    upload_arg_parser = sub_parsers.add_parser("upload")
    upload_arg_parser.add_argument("-a", "--dataset", help="Upload a dataset", nargs=1, action=UploadDatasetAction)
    arg_parser.parse_args()


class InitAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        cwd = os.getcwd()
        project_path = "{}/{}".format(cwd, values) if values is not None else cwd

        if values is not None and os.path.exists(project_path):
            raise Exception("Path {} already exists. Please choose a different project name.".format(project_path))

        create_new_research_project(values)


class LoginAction(argparse.Action):
    def __call__(self, *args, **kwargs):
        login()


class LogoutAction(argparse.Action):
    def __call__(self, *args, **kwargs):
        logout()


class SignupAction(argparse.Action):
    def __call__(self, *args, **kwargs):
        signup()


class DownloadDatasetAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if values is None or len(values) < 1:
            raise Exception("Must provide the name of an existing project.")

        download_dataset(values[0])


class UploadDatasetAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if values is None or len(values) < 1:
            raise Exception("Must provide the name of an existing project.")

        upload_dataset()


if __name__ == "__main__":
    main()
