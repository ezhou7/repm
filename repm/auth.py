import os
import pickle
import requests
from typing import Union

from repm import get_api_url, get_global_file_path


def __get_active_session() -> Union[requests.Session, None]:
    active_session_file_path = get_global_file_path("/active_session.pkl")
    if not os.path.exists(active_session_file_path):
        return None

    with open(active_session_file_path, "r") as fin:
        return pickle.load(fin)


def __set_active_session(active_session: Union[requests.Session, None]):
    active_session_file_path = get_global_file_path("/active_session.pkl")
    with open(active_session_file_path, "w") as fout:
        if active_session:
            pickle.dump(active_session, fout)
        else:
            fout.write("")


def login(email: str, password: str):
    active_session = __get_active_session()
    if active_session:
        print("Already logged in.")
        return

    session = requests.Session()
    login_url = get_api_url("/auth/login")
    login_details = {
        "email": email,
        "password": password
    }
    login_res = session.post(login_url, data=login_details)

    if login_res.status_code == 200:
        __set_active_session(session)
        print("Successfully logged in.")
    elif login_res.status_code == 401:
        print(login_res.content)


def logout():
    active_session = __get_active_session()
    if not active_session:
        print("Already logged out.")
        return

    session_cookies: dict = active_session.cookies.get_dict()

    logout_url = get_api_url("/auth/logout")
    logout_res = active_session.get(logout_url, cookies=session_cookies)

    if logout_res.status_code == 200:
        __set_active_session(None)
        print("Successfully logged out.")
