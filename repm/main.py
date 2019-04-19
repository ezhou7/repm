import sys
from repm.project import create_new_research_project


def main():
    create_new_research_project(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
