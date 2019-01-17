from setuptools import setup, find_packages


def setup_package():
    metadata = dict(
        name="research-package-manager",
        version="1.0.0",
        description="Research package manager",
        packages=find_packages(),
        install_requires=[
            "sh==1.12.14"
        ]
    )

    setup(**metadata)


if __name__ == "__main__":
    setup_package()
