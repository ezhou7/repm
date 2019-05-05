import argparse
from repm.project import create_new_research_project


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-ws", "--workspace", help="workspace name", type=str)
    arg_parser.add_argument("-p", "--package", help="package name", type=str)
    args = arg_parser.parse_args()
    create_new_research_project(args.workspace, args.package)


if __name__ == "__main__":
    main()
