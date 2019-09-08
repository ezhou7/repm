import os
import pickle
from typing import Optional
from requests import Session, Response

from repm import get_api_url, get_global_file_path


def get_active_session() -> Optional[Session]:
    file_path: str = get_global_file_path("active_session.pkl")
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        return None

    with open(file_path, "rb") as fin:
        return pickle.load(fin)


def set_active_session(active_session: Optional[Session]):
    file_path: str = get_global_file_path("active_session.pkl")
    with open(file_path, "wb") as fout:
        if active_session:
            pickle.dump(active_session, fout)


def is_active_session_valid(active_session: Optional[Session]) -> bool:
    if not active_session:
        return False

    session_cookies: dict = active_session.cookies.get_dict()

    is_session_valid_url: str = get_api_url("/auth/isSessionValid")
    is_session_valid_res: Response = active_session.post(is_session_valid_url, cookies=session_cookies)

    return is_session_valid_res.status_code == 200
