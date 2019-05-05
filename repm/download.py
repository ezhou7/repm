import boto3


def download_research_code_package(org_name: str, package_name: str):
    # TODO: implement this method
    # search for research code
    # if found, download package, else return error message and closest matches
    pass


def download_research_dataset(org_name: str, dataset_name: str):
    s3_client = boto3.resource("s3")
    bucket_name = "zephyr/{}/datasets/{}".format(org_name, dataset_name)
    bucket = s3_client.Bucket(bucket_name)
    bucket.download_file(dataset_name)


def download_research_project(org_name: str):
    # TODO: implement this method
    # search for research project
    # if found, download project code package and dataset, else return error message and closest matches
    # ask if user wishes to download code, dataset or both code and dataset
    pass
