import os
import argparse
from repm.project import create_new_research_project


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-i", "--init", help="Initialize current directory as a new research project",
                            nargs="?", action=InitAction)
    arg_parser.parse_args()


class InitAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        cwd = os.getcwd()
        project_path = "{}/{}".format(cwd, values) if values is not None else cwd

        if values is not None and os.path.exists(project_path):
            raise Exception("Path {} already exists. Please choose a different project name.".format(project_path))

        create_new_research_project(values)


if __name__ == "__main__":
    main()
