import os

from repm import get_api_url
from repm.dirutils import get_repm_project_root_directory
from repm.auth import __get_active_session, __is_active_session_valid


def upload_dataset(dataset_name: str):
    active_session = __get_active_session()
    if not __is_active_session_valid(active_session):
        print("You must login before uploading any data.")
        return

    session_cookies: dict = active_session.cookies.get_dict()
    upload_url: str = get_api_url("/dataset")

    project_root_path: str = get_repm_project_root_directory()
    if project_root_path:
        upload_path: str = "{}/data/{}/".format(project_root_path, dataset_name)
    else:
        raise Exception("Not within a repm project")

    upload_details = {"bucketName": dataset_name}

    for filename in os.listdir(upload_path):
        file_path = os.path.join(upload_path, filename)
        session_files = {
            "file": (
                filename,
                open(file_path, "rb"),
                "application/octet-stream"
            )
        }
        res = active_session.post(
            upload_url,
            data=upload_details,
            files=session_files,
            cookies=session_cookies
        )
        print(res.content.decode("utf-8"))
