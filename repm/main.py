import os
import argparse
from repm.project import create_new_research_project
from repm.download import download_research_dataset


def main():
    arg_parser = argparse.ArgumentParser()
    sub_parsers = arg_parser.add_subparsers()
    arg_parser.add_argument("-i", "--init", help="Initialize current directory as a new research project",
                            nargs="?", action=InitAction)
    download_arg_parser = sub_parsers.add_parser("download")
    download_arg_parser.add_argument("-a", "--dataset", help="Download the dataset(s) from a project", nargs=1,
                                     action=DownloadDatasetAction)
    arg_parser.parse_args()


class InitAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        cwd = os.getcwd()
        project_path = "{}/{}".format(cwd, values) if values is not None else cwd

        if values is not None and os.path.exists(project_path):
            raise Exception("Path {} already exists. Please choose a different project name.".format(project_path))

        create_new_research_project(values)


class DownloadDatasetAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if values is None or len(values) < 1:
            raise Exception("Must provide the name of an existing project.")

        download_research_dataset(values[0])


if __name__ == "__main__":
    main()
