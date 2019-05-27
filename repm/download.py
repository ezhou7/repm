import os
import re
from google.cloud import storage

from repm.dirutils import get_repm_project_root_directory


def download_research_dataset(dataset_name: str):
    storage_client = storage.Client.create_anonymous_client()
    bucket = storage_client.bucket(dataset_name)

    project_root_path = get_repm_project_root_directory()
    if project_root_path:
        download_path = "{}/data/{}/".format(project_root_path, dataset_name)
        if not os.path.exists(download_path):
            os.mkdir(download_path)
    else:
        raise Exception("Not within a repm project")

    for blob in bucket.list_blobs():
        file_path = os.path.join(download_path, os.path.basename(blob.name))
        bucket.blob(blob.name).download_to_filename(file_path)
