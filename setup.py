from setuptools import setup, find_packages


def setup_package():
    metadata = dict(
        name="repm",
        version="1.0.0",
        description="repm",
        packages=find_packages(),
        package_data={
            "repm": ["resources/*"]
        },
        include_package_data=True,
        entry_points={
            "console_scripts": [
                "repm = repm.main:main"
            ]
        },
        install_requires=[
            "sh",
            "google-cloud-storage",
            "argparse"
        ]
    )

    setup(**metadata)


if __name__ == "__main__":
    setup_package()
