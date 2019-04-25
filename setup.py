from glob import glob
from setuptools import setup, find_packages


def setup_package():
    metadata = dict(
        name="repm",
        version="1.0.0",
        description="repm",
        packages=find_packages(),
        data_files=[
            ("bin", glob("bin/*")),
            ("resources", glob("resources/*"))
        ],
        include_package_data=True,
        entry_points={
            "console_scripts": [
                "repm = repm.__main__:main"
            ]
        },
        install_requires=[
            "sh",
            "boto3"
        ]
    )

    setup(**metadata)


if __name__ == "__main__":
    setup_package()
