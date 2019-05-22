import os
import re
from google.cloud import storage

from repm.dirutils import get_repm_project_root_directory


def download_research_code_package(org_name: str, package_name: str):
    # TODO: implement this method
    # search for research code
    # if found, download package, else return error message and closest matches
    pass


def download_research_dataset(org_name: str, dataset_name: str):
    storage_client = storage.Client.create_anonymous_client()
    bucket = storage_client.bucket("zephyr")

    project_root_path = get_repm_project_root_directory()
    if project_root_path:
        download_path = "{}/data/{}/".format(project_root_path, dataset_name)
        if not os.path.exists(download_path):
            os.mkdir(download_path)
    else:
        raise Exception("Not within a repm project")

    dataset_path = "{}/datasets/{}/.+".format(org_name, dataset_name)
    dataset_path_regex = re.compile(dataset_path)

    for blob in bucket.list_blobs():
        if dataset_path_regex.match(blob.name):
            bucket.blob(blob.name).download_to_filename(os.path.join(download_path, os.path.basename(blob.name)))


def download_research_project(org_name: str):
    # TODO: implement this method
    # search for research project
    # if found, download project code package and dataset, else return error message and closest matches
    # ask if user wishes to download code, dataset or both code and dataset
    pass
