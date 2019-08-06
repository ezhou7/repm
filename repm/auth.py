import os
import pickle
import getpass
import requests
from typing import Union

from repm import get_api_url, get_global_file_path


def __get_active_session() -> Union[requests.Session, None]:
    file_path = get_global_file_path("active_session.pkl")
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        return None

    with open(file_path, "rb") as fin:
        return pickle.load(fin)


def __set_active_session(active_session: Union[requests.Session, None]):
    file_path = get_global_file_path("active_session.pkl")
    with open(file_path, "wb") as fout:
        if active_session:
            pickle.dump(active_session, fout)


def login():
    active_session = __get_active_session()
    if active_session:
        print("Already logged in.")
        return

    email: str = input("Email: ")
    password: str = getpass.getpass("Password: ")

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
    else:
        print(login_res.content.decode("utf-8"))


def logout():
    active_session = __get_active_session()
    if not active_session:
        print("Not logged in.")
        return

    session_cookies: dict = active_session.cookies.get_dict()

    logout_url = get_api_url("/auth/logout")
    logout_res = active_session.get(logout_url, cookies=session_cookies)

    if logout_res.status_code == 200:
        __set_active_session(None)
        print("Successfully logged out.")
    else:
        print(logout_res.content.decode("utf-8"))


def signup():
    active_session = __get_active_session()
    if active_session:
        print("Please log out before signing up for a new account.")
        return

    email: str = input("Email: ")
    password: str = getpass.getpass("Password: ")

    active_session = requests.Session()
    signup_url = get_api_url("/auth/signup")
    signup_details = {
        "email": email,
        "password": password
    }
    signup_res = active_session.post(signup_url, data=signup_details)
    print(signup_res.content.decode("utf-8"))
