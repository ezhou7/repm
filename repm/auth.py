import getpass
from requests import Session, Response

from repm import get_api_url
from repm.session import get_active_session, set_active_session, is_active_session_valid


def login():
    active_session = get_active_session()
    if is_active_session_valid(active_session):
        print("Already logged in.")
        return

    email: str = input("Email: ")
    password: str = getpass.getpass("Password: ")

    session = Session()
    login_url = get_api_url("/auth/login")
    login_details = {
        "email": email,
        "password": password
    }
    login_res: Response = session.post(login_url, data=login_details)

    if login_res.status_code == 200:
        set_active_session(session)

    print(login_res.content.decode("utf-8"))


def logout():
    active_session = get_active_session()
    if not is_active_session_valid(active_session):
        print("Not logged in.")
        return

    session_cookies: dict = active_session.cookies.get_dict()

    logout_url: str = get_api_url("/auth/logout")
    logout_res: Response = active_session.get(logout_url, cookies=session_cookies)

    if logout_res.status_code == 200:
        set_active_session(None)

    print(logout_res.content.decode("utf-8"))


def signup():
    active_session = get_active_session()
    if is_active_session_valid(active_session):
        print("Please log out before signing up for a new account.")
        return

    email: str = input("Email: ")
    password: str = getpass.getpass("Password: ")

    active_session = Session()
    signup_url: str = get_api_url("/auth/signup")
    signup_details = {
        "email": email,
        "password": password
    }
    signup_res: Response = active_session.post(signup_url, data=signup_details)
    print(signup_res.content.decode("utf-8"))
