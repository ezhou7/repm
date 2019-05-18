from google.cloud import storage

from repm.dirutils import get_repm_project_root_directory


def download_research_code_package(org_name: str, package_name: str):
    # TODO: implement this method
    # search for research code
    # if found, download package, else return error message and closest matches
    pass


def download_research_dataset(org_name: str, dataset_name: str):
    storage_client = storage.Client()
    bucket_name = "zephyr/{}/datasets/{}".format(org_name, dataset_name)
    bucket = storage_client.get_bucket(bucket_name)

    project_root_path = get_repm_project_root_directory()
    if project_root_path:
        download_path = "{}/data".format(project_root_path)
    else:
        raise Exception("Not within a repm project")

    bucket.blob(dataset_name).download_to_filename(download_path)


def download_research_project(org_name: str):
    # TODO: implement this method
    # search for research project
    # if found, download project code package and dataset, else return error message and closest matches
    # ask if user wishes to download code, dataset or both code and dataset
    pass
