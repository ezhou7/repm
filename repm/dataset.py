import requests

from repm import get_api_url


def list_datasets():
    list_datasets_url: str = get_api_url("/datasets/list")
    list_datasets_res = requests.get(list_datasets_url)

    if list_datasets_res.status_code == 200:
        dataset_names = list_datasets_res.json()

        for name in dataset_names:
            print(name)
    else:
        print(list_datasets_res.content.decode("utf-8"))
