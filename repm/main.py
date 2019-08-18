import os
from argparse import ArgumentParser, Action
from repm.project import create_new_research_project
from repm.download import download_dataset
from repm.upload import upload_dataset
from repm.auth import login, logout, signup
from repm.dataset import list_datasets


def main():
    arg_parser = ArgumentParser()

    # main arguments
    arg_parser.add_argument("-i", "--init", help="Initialize current directory as a new research project",
                            nargs="?", action=InitAction)
    arg_parser.add_argument("-l", "--login", help="Login with a username and password", nargs=0, action=LoginAction)
    arg_parser.add_argument("-o", "--logout", help="Logout of a session", nargs=0, action=LogoutAction)
    arg_parser.add_argument("-s", "--signup", help="Signup with a username and password", nargs=0, action=SignupAction)
    arg_parser.add_argument("-t", "--list", help="List all publich datasets", nargs=0, action=ListDatasetsAction)

    sub_parsers = arg_parser.add_subparsers()

    # main arguments w/ sub commands
    download_arg_parser = sub_parsers.add_parser("download")
    download_arg_parser.add_argument("-a", "--dataset", help="Download the dataset from a project", nargs=1,
                                     action=DownloadDatasetAction)
    upload_arg_parser = sub_parsers.add_parser("upload")
    upload_arg_parser.add_argument("-a", "--dataset", help="Upload a dataset", nargs=1, action=UploadDatasetAction)
    arg_parser.parse_args()


class InitAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        cwd = os.getcwd()
        project_path = "{}/{}".format(cwd, values) if values is not None else cwd

        if values is not None and os.path.exists(project_path):
            raise Exception("Path {} already exists. Please choose a different project name.".format(project_path))

        create_new_research_project(values[0])


class LoginAction(Action):
    def __call__(self, *args, **kwargs):
        login()


class LogoutAction(Action):
    def __call__(self, *args, **kwargs):
        logout()


class SignupAction(Action):
    def __call__(self, *args, **kwargs):
        signup()


class ListDatasetsAction(Action):
    def __call__(self, *args, **kwargs):
        list_datasets()


class DownloadDatasetAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if values is None or len(values) < 1:
            raise Exception("Must provide the name of an existing project.")

        download_dataset(values[0])


class UploadDatasetAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if values is None or len(values) < 1:
            raise Exception("Must provide the name of an existing project.")

        upload_dataset(values[0])


if __name__ == "__main__":
    main()
