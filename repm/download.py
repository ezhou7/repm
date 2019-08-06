import os
import zipfile
import requests

from repm import get_api_url
from repm.dirutils import get_repm_project_root_directory


def download_dataset(dataset_name: str):
    download_url: str = get_api_url("/dataset")

    project_root_path: str = get_repm_project_root_directory()
    if project_root_path:
        download_path = "{}/data/{}/".format(project_root_path, dataset_name)
    else:
        raise Exception("Not within a repm project")

    print("Downloading...")
    download_path: str = __download_zip(dataset_name, download_url, download_path)
    print("Finished download: {}".format(download_path))


def __download_zip(dataset_name: str, url: str, download_path: str):
    download_params = {"bucketName": dataset_name}
    with requests.get(url, params=download_params, stream=True) as response:
        response.raise_for_status()
        zip_path: str = download_path[:-1] + ".zip"

        with open(zip_path, "wb") as fout:
            for chunk in response.iter_content(chunk_size=8192):
                # filter out keep-alive new chunks
                if chunk:
                    fout.write(chunk)
            fout.flush()

    fzip = zipfile.ZipFile(zip_path, "r")
    fzip.extractall(download_path)
    fzip.close()

    os.remove(zip_path)

    return download_path
