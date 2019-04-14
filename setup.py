from glob import glob
from setuptools import setup, find_packages


def setup_package():
    metadata = dict(
        name="rpm",
        version="1.0.0",
        description="rpm",
        packages=find_packages(),
        data_files=[
            ("bin", glob("bin/*")),
            ("resources", glob("resources/*"))
        ],
        include_package_data=True,
        install_requires=[
            "sh==1.12.14"
        ]
    )

    setup(**metadata)


if __name__ == "__main__":
    setup_package()
