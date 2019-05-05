from glob import glob
from setuptools import setup, find_packages


def setup_package():
    metadata = dict(
        name="{0}",
        version="1.0.0",
        description="{0}",
        packages=find_packages(),
        data_files=[
            ("config", glob("config/*")),
            ("resources", glob("resources/*"))
        ],
        install_requires=[]
    )

    setup(**metadata)


if __name__ == "__main__":
    setup_package()
